from django.contrib import admin
from .models import (
    Medicine, DonationRequest, UserProfile, MedicineRating, MedicineSearchLog, 
    Notification, ContactMessage, Testimonial, FAQ, PasswordResetToken, PickupDelivery,
    DeliveryBoy, Delivery, DeliveryLocation
)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'organization_name', 'verified', 'created_at')
    list_filter = ('role', 'verified', 'created_at')
    search_fields = ('user__username', 'user__email', 'organization_name')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'donor', 'quantity', 'expiry_date', 'status', 'rating', 'created_at')
    list_filter = ('status', 'created_at', 'expiry_date')
    search_fields = ('name', 'donor__username', 'description')
    readonly_fields = ('created_at', 'updated_at', 'viewed_by')
    fieldsets = (
        ('Basic Information', {
            'fields': ('donor', 'name', 'description', 'image')
        }),
        ('Quantity & Storage', {
            'fields': ('quantity', 'unit', 'storage_condition')
        }),
        ('Dates', {
            'fields': ('expiry_date', 'manufacture_date')
        }),
        ('Batch & Location', {
            'fields': ('batch_number', 'location_name', 'latitude', 'longitude')
        }),
        ('Status & Rating', {
            'fields': ('status', 'rating', 'rating_count', 'recommendation_score')
        }),
        ('Tracking', {
            'fields': ('viewed_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(DonationRequest)
class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'medicine', 'ngo', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'medicine__donor')
    search_fields = ('medicine__name', 'ngo__username', 'medicine__donor__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Request Details', {
            'fields': ('medicine', 'ngo', 'status')
        }),
        ('Request Info', {
            'fields': ('quantity_requested', 'message')
        }),
        ('Tracking', {
            'fields': ('created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(MedicineRating)
class MedicineRatingAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('medicine__name', 'user__username', 'review')
    readonly_fields = ('created_at',)

@admin.register(MedicineSearchLog)
class MedicineSearchLogAdmin(admin.ModelAdmin):
    list_display = ('search_query', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('search_query', 'user__username')
    readonly_fields = ('created_at',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('title', 'message', 'user__username')
    readonly_fields = ('created_at',)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_resolved', 'created_at')
    list_filter = ('is_resolved', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'approved', 'created_at')
    list_filter = ('role', 'approved', 'created_at')
    search_fields = ('name', 'message', 'user__username')
    readonly_fields = ('created_at',)
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} testimonials approved.")
    approve_testimonials.short_description = "Approve selected testimonials"

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order', 'active')
    list_filter = ('category', 'active')
    search_fields = ('question', 'answer')
    list_editable = ('order', 'active')
    ordering = ('order',)

@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'expires_at', 'used')
    list_filter = ('used', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('token', 'created_at')

@admin.register(PickupDelivery)
class PickupDeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'medicine', 'donor', 'ngo', 'status', 'quantity_scheduled', 'created_at')
    list_filter = ('status', 'created_at', 'donor', 'ngo')
    search_fields = ('medicine__name', 'donor__username', 'ngo__username')
    readonly_fields = ('created_at', 'updated_at', 'days_since_created')
    fieldsets = (
        ('Request Link', {
            'fields': ('donation_request',)
        }),
        ('Parties', {
            'fields': ('donor', 'ngo', 'medicine')
        }),
        ('Pickup Information', {
            'fields': ('scheduled_pickup_date', 'pickup_date', 'quantity_picked_up', 'pickup_notes')
        }),
        ('Delivery Information', {
            'fields': ('delivery_date', 'quantity_delivered', 'delivery_notes')
        }),
        ('Status & Tracking', {
            'fields': ('status', 'quantity_scheduled', 'created_at', 'updated_at', 'days_since_created'),
            'classes': ('collapse',)
        })
    )

@admin.register(DeliveryBoy)
class DeliveryBoyAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'vehicle_type', 'is_available', 'total_deliveries', 'completed_deliveries', 'rating', 'verified')
    list_filter = ('is_available', 'vehicle_type', 'verified', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone')
    readonly_fields = ('created_at', 'updated_at', 'last_location_update')
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'phone', 'verified')
        }),
        ('Vehicle Details', {
            'fields': ('vehicle_type', 'vehicle_registration')
        }),
        ('Availability & Location', {
            'fields': ('is_available', 'current_latitude', 'current_longitude', 'last_location_update')
        }),
        ('Statistics', {
            'fields': ('total_deliveries', 'completed_deliveries', 'rating'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickup_delivery', 'delivery_boy', 'status', 'assigned_at', 'delivered_at')
    list_filter = ('status', 'assigned_at', 'delivered_at')
    search_fields = ('delivery_boy__user__username', 'pickup_delivery__medicine__name')
    readonly_fields = ('assigned_at', 'created_at', 'updated_at')
    fieldsets = (
        ('Delivery Assignment', {
            'fields': ('pickup_delivery', 'delivery_boy', 'status')
        }),
        ('Timeline', {
            'fields': ('assigned_at', 'picked_up_at', 'started_at', 'delivered_at')
        }),
        ('Details', {
            'fields': ('estimated_delivery_time', 'notes')
        }),
        ('Rating & Review', {
            'fields': ('rating', 'review')
        }),
        ('Tracking', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(DeliveryLocation)
class DeliveryLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery', 'latitude', 'longitude', 'timestamp')
    list_filter = ('timestamp', 'delivery')
    search_fields = ('delivery__id',)
    readonly_fields = ('timestamp',)
    ordering = ['-timestamp']

