from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class UserProfile(models.Model):
    ROLE_CHOICES = [('donor', 'Donor'), ('ngo', 'NGO'), ('delivery_boy', 'Delivery Boy'), ('admin', 'Admin')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='donor')
    phone = models.CharField(max_length=20, blank=True, null=True)
    organization_name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"


class Medicine(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('requested', 'Requested'),
        ('donated', 'Donated'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled')
    ]
    
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medicines')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    unit = models.CharField(max_length=20, default='units')
    expiry_date = models.DateField()
    manufacture_date = models.DateField(blank=True, null=True)
    batch_number = models.CharField(max_length=100, blank=True, null=True)
    storage_condition = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    image = models.ImageField(upload_to='medicines/', null=True, blank=True)
    
    # AI/Recommendation fields
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating_count = models.IntegerField(default=0)
    recommendation_score = models.FloatField(default=0)
    
    # Tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    viewed_by = models.ManyToManyField(User, related_name='viewed_medicines', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
    
    def days_until_expiry(self):
        from datetime import date
        return (self.expiry_date - date.today()).days
    
    def is_expiring_soon(self):
        return 0 <= self.days_until_expiry() <= 30
    
    def is_expired(self):
        from datetime import date
        return self.expiry_date < date.today()


class MedicineRating(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('medicine', 'user')

    def __str__(self):
        return f"{self.medicine.name} - {self.rating}/5"


class DonationRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='requests')
    ngo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donation_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    message = models.TextField(blank=True, null=True)
    quantity_requested = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.ngo.username} requested {self.medicine.name}"


class MedicineSearchLog(models.Model):
    """AI: Track search patterns for recommendations"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    search_query = models.CharField(max_length=200)
    medicine_results = models.ManyToManyField(Medicine, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search: {self.search_query}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    donation_request = models.ForeignKey(DonationRequest, on_delete=models.SET_NULL, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Testimonial(models.Model):
    """User testimonials and success stories"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='testimonials', null=True, blank=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[('donor', 'Medicine Donor'), ('ngo', 'NGO/Hospital')])
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.role}"


class FAQ(models.Model):
    """Frequently Asked Questions"""
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('donation', 'How to Donate'),
        ('request', 'How to Request'),
        ('safety', 'Safety & Guidelines'),
        ('technical', 'Technical Support'),
        ('other', 'Other')
    ])
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class PasswordResetToken(models.Model):
    """Password reset tokens"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reset_tokens')
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"Reset token for {self.user.username}"

class PickupDelivery(models.Model):
    """Track pickup and delivery of medicines from donor to NGO/Hospital"""
    STATUS_CHOICES = [
        ('pending', 'Pending Pickup'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]
    
    donation_request = models.OneToOneField(DonationRequest, on_delete=models.CASCADE, related_name='pickup_delivery')
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pickups_given')
    ngo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pickups_received')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='pickups')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Pickup details
    scheduled_pickup_date = models.DateTimeField(null=True, blank=True)
    pickup_date = models.DateTimeField(null=True, blank=True)
    pickup_notes = models.TextField(blank=True, null=True)
    
    # Delivery details
    delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_notes = models.TextField(blank=True, null=True)
    
    # Quantities
    quantity_scheduled = models.IntegerField()
    quantity_picked_up = models.IntegerField(null=True, blank=True, default=0)
    quantity_delivered = models.IntegerField(null=True, blank=True, default=0)
    
    # Tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Pickup/Delivery - {self.medicine.name} ({self.status})"
    
    def days_since_created(self):
        from datetime import date
        return (date.today() - self.created_at.date()).days


class DeliveryBoy(models.Model):
    """
    DeliveryBoy model for delivery personnel who transport medicines.
    Extends the User model with delivery-specific information.
    """
    VEHICLE_CHOICES = [
        ('bike', 'Motorcycle'),
        ('scooter', 'Scooter'),
        ('car', 'Car'),
        ('van', 'Van'),
        ('bicycle', 'Bicycle'),
        ('on_foot', 'On Foot')
    ]
    
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('offline', 'Offline')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_boy')
    phone = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    vehicle_registration = models.CharField(max_length=50, blank=True, null=True)
    is_available = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='offline')
    current_latitude = models.FloatField(null=True, blank=True)
    current_longitude = models.FloatField(null=True, blank=True)
    total_deliveries = models.IntegerField(default=0)
    completed_deliveries = models.IntegerField(default=0)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_location_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name or self.user.username} - {self.get_is_available_display()}"
    
    def get_completion_rate(self):
        """Calculate delivery completion rate"""
        if self.total_deliveries == 0:
            return 0
        return (self.completed_deliveries / self.total_deliveries) * 100


class Delivery(models.Model):
    """
    Delivery model tracking medicine transport from donor to NGO/Hospital.
    Links to PickupDelivery and manages delivery boy assignment and status.
    """
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]
    
    pickup_delivery = models.OneToOneField(PickupDelivery, on_delete=models.CASCADE, related_name='delivery')
    delivery_boy = models.ForeignKey(DeliveryBoy, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')
    assigned_at = models.DateTimeField(auto_now_add=True)
    picked_up_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    estimated_delivery_time = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Delivery - {self.pickup_delivery.medicine.name} ({self.status})"
    
    def get_duration_minutes(self):
        """Get delivery duration in minutes"""
        if self.delivered_at and self.started_at:
            duration = self.delivered_at - self.started_at
            return int(duration.total_seconds() / 60)
        return None


class DeliveryLocation(models.Model):
    """
    Real-time location tracking for deliveries.
    Stores latitude, longitude, and timestamp for every location update.
    """
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='locations')
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.FloatField(null=True, blank=True)  # GPS accuracy in meters
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Delivery Locations"

    def __str__(self):
        return f"Location - {self.delivery.id} at {self.timestamp}"
    
    def get_coordinates(self):
        """Return coordinates as tuple"""
        return (self.latitude, self.longitude)
