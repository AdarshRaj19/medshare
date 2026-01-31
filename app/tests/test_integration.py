from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import get_user_model
from app.models import UserProfile, Medicine, DonationRequest, DeliveryBoy, PickupDelivery, Delivery

User = get_user_model()

class IntegrationFlowTests(TestCase):
    def setUp(self):
        self.client = Client()
        # create users
        self.donor = User.objects.create_user(username='int_donor', password='testpass')
        UserProfile.objects.update_or_create(user=self.donor, defaults={'role':'donor'})

        self.ngo = User.objects.create_user(username='int_ngo', password='testpass')
        UserProfile.objects.update_or_create(user=self.ngo, defaults={'role':'ngo'})

        self.db_user = User.objects.create_user(username='int_delivery', password='testpass')
        UserProfile.objects.update_or_create(user=self.db_user, defaults={'role':'delivery_boy'})
        self.delivery_boy = DeliveryBoy.objects.create(user=self.db_user, phone='000', vehicle_type='bike', is_available='available')

        expiry = (timezone.now() + timedelta(days=365)).date()
        self.med = Medicine.objects.create(donor=self.donor, name='IntMed', quantity=5, expiry_date=expiry)

        # create accepted donation request
        self.req = DonationRequest.objects.create(medicine=self.med, ngo=self.ngo, status='accepted')

    def test_create_pickup_and_claim_via_http(self):
        # donor logs in and creates pickup via POST
        self.client.login(username='int_donor', password='testpass')
        url = reverse('create_pickup_delivery', args=[self.req.id])
        resp = self.client.post(url, {'scheduled_pickup_date': '', 'pickup_notes': 'Test pickup'})
        # Expect redirect to pickup detail or dashboard
        self.assertIn(resp.status_code, (302, 200))

        # PickupDelivery should exist
        pickup = PickupDelivery.objects.filter(donation_request=self.req).first()
        self.assertIsNotNone(pickup)
        self.assertEqual(pickup.status, 'pending')

        # delivery boy logs in and claims via POST
        self.client.logout()
        self.client.login(username='int_delivery', password='testpass')
        claim_url = reverse('claim_pickup')
        resp2 = self.client.post(claim_url, {'pickup_id': pickup.id})
        # Expect redirect
        self.assertIn(resp2.status_code, (302, 200))

        # Delivery should now exist and assigned to delivery_boy
        delivery = Delivery.objects.filter(pickup_delivery=pickup).first()
        self.assertIsNotNone(delivery)
        self.assertEqual(delivery.delivery_boy, self.delivery_boy)
        self.delivery_boy.refresh_from_db()
        self.assertEqual(self.delivery_boy.is_available, 'busy')
