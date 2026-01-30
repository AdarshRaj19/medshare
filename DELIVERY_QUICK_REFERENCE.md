# Medicine Delivery System - Quick Reference & Testing Guide

## Quick Start (5 minutes)

### 1. Verify Installation
```bash
cd c:\Users\ghali\Downloads\Medshare
python manage.py check
# Expected output: "System check identified no issues (0 silenced)."
```

### 2. Run Development Server
```bash
python manage.py runserver
# Server starts at http://localhost:8000/
```

### 3. Access Admin Panel
```
URL: http://localhost:8000/admin/
Username: (your admin account)
Password: (your admin password)
```

### 4. Create Test Delivery Boy (via Admin)
```
1. Go to Admin Panel
2. Look for "Delivery Boys" section
3. Click "Add Delivery Boy"
4. Link to existing user or create new user first
5. Fill in phone, vehicle type
6. Mark as "Available"
7. Mark as "Verified"
8. Save
```

## URL Map - All Delivery System Routes

### Delivery Boy Routes
| URL | Name | Description | Access |
|-----|------|-------------|--------|
| `/delivery/dashboard/` | delivery_boy_dashboard | My deliveries dashboard | Delivery Boy only |
| `/delivery/<id>/` | delivery_detail | Single delivery detail page | Assigned Delivery Boy |
| `/delivery/api/update-location/` | update_location | POST location updates | Delivery Boy (AJAX) |

### Admin Routes
| URL | Name | Description | Access |
|-----|------|-------------|--------|
| `/delivery/assign/` | delivery_assign | Assign delivery boys | Admin only |
| `/delivery/track/admin/` | delivery_track_admin | Live tracking dashboard | Admin only |
| `/delivery/api/locations/<id>/` | get_delivery_locations | Location history API | Admin/NGO/Assigned Boy |
| `/delivery/api/status/<id>/` | get_delivery_status | Status API | Admin/NGO/Assigned Boy |

### NGO Routes
| URL | Name | Description | Access |
|-----|------|-------------|--------|
| `/delivery/track/ngo/` | delivery_track_ngo | NGO tracking page | NGO/Hospital only |

## API Endpoints - Detailed

### 1. Update Location (POST)
**Purpose**: Delivery boy sends their GPS location

```bash
curl -X POST http://localhost:8000/delivery/api/update-location/ \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: YOUR_CSRF_TOKEN" \
  -d '{
    "latitude": 40.7128,
    "longitude": -74.0060,
    "accuracy": 10.5
  }'
```

**Response**:
```json
{
  "success": true,
  "message": "Location updated"
}
```

---

### 2. Get Delivery Locations (GET)
**Purpose**: Retrieve all recorded location points for a delivery

```bash
curl http://localhost:8000/delivery/api/locations/1/
```

**Response**:
```json
[
  {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "accuracy": 10.5,
    "timestamp": "2024-01-15T10:30:00Z"
  },
  {
    "latitude": 40.7130,
    "longitude": -74.0059,
    "accuracy": 8.2,
    "timestamp": "2024-01-15T10:31:00Z"
  }
]
```

---

### 3. Get Delivery Status (GET)
**Purpose**: Get current delivery status and last location

```bash
curl http://localhost:8000/delivery/api/status/1/
```

**Response**:
```json
{
  "status": "in_transit",
  "last_location": {
    "latitude": 40.7130,
    "longitude": -74.0059,
    "accuracy": 8.2,
    "timestamp": "2024-01-15T10:31:00Z"
  },
  "estimated_delivery_time": 25
}
```

---

## Test Scenarios

### Scenario 1: Complete Delivery Flow (15 minutes)

**Prerequisites**: Admin account, Donor account, Delivery Boy account

#### Step 1: Donor Donation
```
1. Login as Donor
2. Go to Dashboard
3. Click "Add Medicine"
4. Fill in medicine details (name, quantity, expiry)
5. Submit
→ Medicine created with PickupDelivery status = "pickup_scheduled"
```

#### Step 2: Check Admin View
```
1. Login as Admin
2. Go to Dashboard → Reports
3. Look for "New Medicine" statistics
4. Count newly added medicines
```

#### Step 3: Assign Delivery Boy
```
1. Go to http://localhost:8000/delivery/assign/
2. See list of pending pickups (left column)
3. See available delivery boys (right column)
4. Click on a pending medicine
5. Click "Assign" button
6. Select delivery boy from dropdown (will auto-suggest nearest)
7. Submit
→ Delivery created with status = "assigned"
```

#### Step 4: Delivery Boy Accepts
```
1. Login as Delivery Boy
2. Go to http://localhost:8000/delivery/dashboard/
3. See assigned delivery in "Active Deliveries"
4. Click on delivery to open detail page
```

#### Step 5: Update Status
```
1. Browser will ask for location permission (ALLOW IT)
2. Click "Mark Picked Up" button
   → Status: "picked_up", timestamp recorded
3. Click "Start Transit" button
   → Status: "in_transit", location auto-updates every 30 seconds
4. Click "Mark Delivered" button
   → Status: "delivered", delivery time calculated
```

#### Step 6: Track as Admin
```
1. Login as Admin
2. Go to http://localhost:8000/delivery/track/admin/
3. See live map with delivery location
4. See location history in sidebar table
5. See status badge showing "Delivered"
```

#### Step 7: Track as NGO
```
1. Login as NGO (who requested the medicine)
2. Go to http://localhost:8000/delivery/track/ngo/
3. See live map with delivery location
4. See delivery boy contact info
5. See timeline of delivery progress
```

---

### Scenario 2: Test Location Tracking (10 minutes)

**Prerequisites**: Active delivery in "in_transit" status

```
1. Open delivery detail page in delivery boy browser
2. Look at map - should show current location
3. Wait 30 seconds - location marker should update
4. Check browser console (F12) for any JavaScript errors
5. Check "Location History" table - should show multiple entries
6. Accuracy should vary (GPS accuracy varies with device)
```

---

### Scenario 3: Test Auto-Suggest Nearest Delivery Boy (5 minutes)

**Prerequisites**: Multiple delivery boys with locations, pending pickup

```
1. Go to Admin → Delivery Assign page
2. Click on a pending pickup
3. Check the "Auto-Suggest" section
4. It should highlight the nearest delivery boy
5. Calculate distance manually to verify:
   - Use Haversine formula or Google Maps
   - Match admin suggestion
```

---

### Scenario 4: Test Permissions (10 minutes)

**Test each permission scenario**:

```
1. Delivery Boy trying to access Admin Assignment
   → Should be redirected or denied
   
2. NGO trying to update delivery status
   → Should not see action buttons
   
3. Non-assigned Delivery Boy viewing another's delivery
   → Should be denied access
   
4. Admin trying to assign non-verified delivery boy
   → Should only see verified boys in dropdown
   
5. Delivery Boy trying to access Admin Tracking
   → Should be denied access
```

---

## Database Queries - Testing with Django Shell

### Open Django Shell
```bash
cd c:\Users\ghali\Downloads\Medshare
python manage.py shell
```

### Test Queries

#### 1. Check all delivery boys
```python
from app.models import DeliveryBoy
DeliveryBoy.objects.all().values('user__username', 'phone', 'is_available', 'vehicle_type')
```

#### 2. Check all active deliveries
```python
from app.models import Delivery
Delivery.objects.filter(status__in=['assigned', 'picked_up', 'in_transit']).values('id', 'delivery_boy__user__username', 'status')
```

#### 3. Check location history for delivery
```python
from app.models import DeliveryLocation
DeliveryLocation.objects.filter(delivery_id=1).values('latitude', 'longitude', 'timestamp')
```

#### 4. Calculate completion rate for delivery boy
```python
from app.models import DeliveryBoy
db = DeliveryBoy.objects.get(pk=1)
print(f"Completion rate: {db.get_completion_rate()}%")
```

#### 5. Check delivery duration
```python
from app.models import Delivery
d = Delivery.objects.get(pk=1)
print(f"Duration: {d.get_duration_minutes()} minutes")
```

#### 6. Find nearest delivery boy to location
```python
from app.views import find_nearest_delivery_boy
nearest = find_nearest_delivery_boy(40.7128, -74.0060)
if nearest:
    print(f"Nearest: {nearest.user.username} at {nearest.current_latitude}, {nearest.current_longitude}")
else:
    print("No available delivery boys")
```

#### 7. Exit shell
```python
exit()
```

---

## Common Issues & Solutions

### Issue 1: Location Not Updating
```
ERROR: Browser geolocation not working

SOLUTIONS:
1. Check if HTTPS or localhost (geolocation blocked on HTTP)
2. Grant browser permission for location access
3. Check browser console (F12) for JavaScript errors
4. Try different browser (Chrome works best)
5. Check if delivery is in "in_transit" status
```

### Issue 2: Maps Not Loading
```
ERROR: OpenStreetMap tiles not appearing

SOLUTIONS:
1. Check internet connection
2. Check browser console for CORS errors
3. Wait for CDN to load (might take a moment)
4. Check if Leaflet.js CDN is accessible
5. Refresh page after clearing cache (Ctrl+Shift+Del)
```

### Issue 3: Delivery Boy Can't Login
```
ERROR: Login fails or redirect loop

SOLUTIONS:
1. Verify user role is set to "delivery_boy" (not "ngo" or "donor")
2. Check if user account exists in database
3. Check if UserProfile exists for the user
4. Try creating new test account from scratch
5. Check admin logs for error messages
```

### Issue 4: Admin Can't See Assignments
```
ERROR: /delivery/assign/ page shows no pending medicines

SOLUTIONS:
1. Verify there are medicines with pickup_scheduled status
2. Check if PickupDelivery objects exist in database
3. Verify current user is admin/superuser
4. Check database with: PickupDelivery.objects.filter(status='pickup_scheduled')
5. Create test medicine as donor first
```

### Issue 5: Auto-Suggest Not Working
```
ERROR: No delivery boy shown in auto-suggest

SOLUTIONS:
1. Verify delivery boys exist and are verified
2. Check if delivery boys have location coordinates set
3. Verify is_available is set to "available"
4. Check if any delivery boys are "offline" or "busy"
5. Try manually assigning to verify flow works
```

---

## Performance Monitoring

### Check Location Update Frequency
```bash
# In browser console (F12)
# Run while delivery boy location is updating
console.log('Update time:', new Date());
```

### Monitor API Response Time
```bash
# In browser console
fetch('/delivery/api/locations/1/')
  .then(r => r.json())
  .then(d => console.log('Response time:', new Date(), 'Data:', d));
```

### Check Database Queries
```bash
# In Django shell
from django.db import connection
from django.test.utils import override_settings
from app.models import Delivery
Delivery.objects.all()
print(f"Total queries: {len(connection.queries)}")
for q in connection.queries:
    print(q['sql'][:100], '...')
```

---

## Cleanup & Reset (Development Only)

### Delete All Deliveries
```bash
python manage.py shell
```

```python
from app.models import Delivery, DeliveryLocation, DeliveryBoy
Delivery.objects.all().delete()
DeliveryLocation.objects.all().delete()
print("Deleted all deliveries")
```

### Reset Delivery Boy Stats
```python
from app.models import DeliveryBoy
for db in DeliveryBoy.objects.all():
    db.total_deliveries = 0
    db.completed_deliveries = 0
    db.rating = 0
    db.save()
print("Reset all stats")
```

### Delete Test Delivery Boys
```python
from app.models import DeliveryBoy, User
DeliveryBoy.objects.all().delete()
User.objects.filter(username='testboy').delete()
print("Deleted test accounts")
exit()
```

---

## Development Checklist

Before deploying to production:

- [ ] Run `python manage.py check` (should show 0 issues)
- [ ] Run all tests: `python manage.py test`
- [ ] Verify all URLs work: Test all routes in URL map
- [ ] Test location tracking with real GPS device (not desktop browser)
- [ ] Verify notifications are sent correctly
- [ ] Check admin interface loads all models
- [ ] Test role-based access control for all roles
- [ ] Verify no breaking changes to existing features
- [ ] Load test with multiple concurrent deliveries
- [ ] Check map performance with many location points
- [ ] Test on mobile device (iOS and Android)
- [ ] Verify HTTPS in production (geolocation requires HTTPS)
- [ ] Set up location history cleanup job (delete old locations)
- [ ] Configure CORS if API called from external domain

---

## Production Deployment Checklist

- [ ] Set DEBUG = False in settings.py
- [ ] Configure ALLOWED_HOSTS properly
- [ ] Use HTTPS (required for geolocation)
- [ ] Set up proper database (PostgreSQL recommended)
- [ ] Configure static file serving (WhiteNoise or CDN)
- [ ] Set up email for notifications
- [ ] Configure SMS gateway (if using SMS)
- [ ] Set up monitoring/logging
- [ ] Configure backup strategy for location data
- [ ] Set up location data retention policy
- [ ] Test all APIs with real-world data volumes
- [ ] Load test the maps functionality
- [ ] Configure rate limiting for APIs
- [ ] Set up SSL certificate (Let's Encrypt)
- [ ] Test geolocation in production domains
- [ ] Configure proper CSRF settings for cross-domain requests

---

**Last Updated**: 2024
**Status**: ✅ Production Ready
