from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from app.models import (
    UserProfile, Medicine, DonationRequest, PickupDelivery, DeliveryBoy, Delivery
)

User = get_user_model()

class SmokeFlowTests(TestCase):
    def setUp(self):
        # create users
        self.donor = User.objects.create_user(username='test_donor', password='testpass')
        UserProfile.objects.update_or_create(user=self.donor, defaults={'role':'donor'})

        self.ngo = User.objects.create_user(username='test_ngo', password='testpass')
        UserProfile.objects.update_or_create(user=self.ngo, defaults={'role':'ngo'})

        self.db_user = User.objects.create_user(username='test_delivery', password='testpass')
        UserProfile.objects.update_or_create(user=self.db_user, defaults={'role':'delivery_boy'})

        self.delivery_boy = DeliveryBoy.objects.create(user=self.db_user, phone='000', vehicle_type='bike', is_available='available')

        # medicine
        expiry = (timezone.now() + timedelta(days=365)).date()
        self.med = Medicine.objects.create(donor=self.donor, name='TestMed', quantity=5, expiry_date=expiry)

    def test_pickup_and_delivery_creation_and_claim(self):
        # create donation request accepted
        req = DonationRequest.objects.create(medicine=self.med, ngo=self.ngo, status='accepted')

        # create pickup_delivery
        pickup = PickupDelivery.objects.create(donation_request=req, donor=self.donor, ngo=self.ngo, medicine=self.med, status='pending', quantity_scheduled=1)
        self.assertEqual(pickup.status, 'pending')

        # simulate auto-assignment (what code would do) - assign delivery to available delivery boy
        delivery = Delivery.objects.create(pickup_delivery=pickup, delivery_boy=self.delivery_boy, status='assigned')
        self.assertEqual(delivery.delivery_boy, self.delivery_boy)

        # simulate claim: set delivery_boy busy
        self.delivery_boy.is_available = 'busy'
        self.delivery_boy.save()
        self.assertEqual(DeliveryBoy.objects.get(pk=self.delivery_boy.pk).is_available, 'busy')

        # simulate pickup -> in transit -> delivered
        pickup.status = 'picked_up'
        pickup.pickup_date = timezone.now()
        pickup.quantity_picked_up = 1
        pickup.save()

        delivery.status = 'in_transit'
        delivery.picked_up_at = timezone.now()
        delivery.save()

        delivery.status = 'delivered'
        delivery.delivered_at = timezone.now()
        delivery.save()

        pickup.status = 'delivered'
        pickup.delivery_date = timezone.now()
        pickup.quantity_delivered = 1
        pickup.save()

        # final assertions
        self.assertEqual(Delivery.objects.get(pk=delivery.pk).status, 'delivered')
        self.assertEqual(PickupDelivery.objects.get(pk=pickup.pk).status, 'delivered')
