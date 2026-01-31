from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone
from datetime import timedelta

from app.models import (
    UserProfile, Medicine, DonationRequest, PickupDelivery, Delivery, DeliveryBoy
)

User = get_user_model()

class Command(BaseCommand):
    help = 'Create test data and run a smoke test for pickup/delivery flows'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Create users
            donor, _ = User.objects.get_or_create(username='smoke_donor', defaults={'email':'donor@example.com'})
            donor.set_password('testpass')
            donor.save()
            UserProfile.objects.update_or_create(user=donor, defaults={'role':'donor'})

            ngo, _ = User.objects.get_or_create(username='smoke_ngo', defaults={'email':'ngo@example.com'})
            ngo.set_password('testpass')
            ngo.save()
            UserProfile.objects.update_or_create(user=ngo, defaults={'role':'ngo'})

            db_user, _ = User.objects.get_or_create(username='smoke_delivery', defaults={'email':'delivery@example.com', 'first_name':'Delivery'})
            db_user.set_password('testpass')
            db_user.save()
            UserProfile.objects.update_or_create(user=db_user, defaults={'role':'delivery_boy'})

            # Create DeliveryBoy record
            delivery_boy, created = DeliveryBoy.objects.get_or_create(user=db_user, defaults={'phone':'0000000000','vehicle_type':'bike','is_available':'available'})
            if not created:
                delivery_boy.is_available = 'available'
                delivery_boy.save()

            # Create a medicine
            expiry = (timezone.now() + timedelta(days=365)).date()
            med, _ = Medicine.objects.get_or_create(
                donor=donor,
                name='SmokeTestMedicine',
                defaults={
                    'quantity': 10,
                    'expiry_date': expiry,
                }
            )

            # Create a donation request (accepted)
            req, _ = DonationRequest.objects.get_or_create(medicine=med, ngo=ngo, defaults={'status':'accepted'})
            req.status = 'accepted'
            req.save()

            # Create pickup_delivery
            pickup, created = PickupDelivery.objects.get_or_create(
                donation_request=req,
                defaults={
                    'donor': donor,
                    'ngo': ngo,
                    'medicine': med,
                    'status': 'pending',
                    'quantity_scheduled': 1
                }
            )

            # Simulate auto-assignment: create Delivery assigned to available delivery_boy
            delivery, created = Delivery.objects.get_or_create(pickup_delivery=pickup, defaults={'delivery_boy': delivery_boy, 'status':'assigned'})

            self.stdout.write(self.style.SUCCESS('Smoke test data created:'))
            self.stdout.write(f'  donor={donor.username}, ngo={ngo.username}, delivery_boy={db_user.username}')
            self.stdout.write(f'  medicine={med.name} (id={med.id})')
            self.stdout.write(f'  donation_request id={req.id} status={req.status}')
            self.stdout.write(f'  pickup_delivery id={pickup.id} status={pickup.status}')
            self.stdout.write(f'  delivery id={delivery.id} assigned_to={delivery.delivery_boy.user.username if delivery.delivery_boy else None} status={delivery.status}')

            # Create another donation + pickup to test claim flow
            req2, _ = DonationRequest.objects.get_or_create(medicine=med, ngo=ngo, defaults={'status':'accepted'})
            pickup2, _ = PickupDelivery.objects.get_or_create(donation_request=req2, defaults={'donor':donor,'ngo':ngo,'medicine':med,'quantity_scheduled':1,'status':'pending'})

            # Simulate claim: delivery boy claims pickup2
            claim_delivery, created = Delivery.objects.get_or_create(pickup_delivery=pickup2, defaults={'delivery_boy': delivery_boy, 'status':'assigned'})
            delivery_boy.is_available = 'busy'
            delivery_boy.save()

            self.stdout.write(self.style.SUCCESS('Claim simulation completed:'))
            self.stdout.write(f'  pickup2 id={pickup2.id} claimed_by={delivery_boy.user.username}')

        self.stdout.write(self.style.SUCCESS('Smoke test finished.'))
