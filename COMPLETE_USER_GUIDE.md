# 📚 **COMPLETE USER GUIDE - MEDSHARE PLATFORM**

**Last Updated**: January 31, 2026
**Platform**: MedShare - Medicine Donation & Volunteer Management System
**Version**: 1.0 (Production Ready)

---

## **TABLE OF CONTENTS**

1. [Initial Setup](#initial-setup)
2. [Registration Guide](#registration-guide)
3. [Donor User Guide](#donor-user-guide)
4. [NGO User Guide](#ngo-user-guide)
5. [Delivery Boy Guide](#delivery-boy-guide)
6. [Admin Guide](#admin-guide)
7. [Quick Reference Links](#quick-reference-links)
8. [Troubleshooting](#troubleshooting)

---

## 🚀 **INITIAL SETUP**

### **Step 1: Start the Server**

Open PowerShell and run:

```powershell
# Navigate to project directory
cd d:\Downloads\Medshare

# Activate Python environment
.\.venv\Scripts\Activate.ps1

# Start Django development server
python manage.py runserver

# Expected output:
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
```

### **Step 2: Access the Website**

Open your web browser and navigate to:

- **Home Page**: http://127.0.0.1:8000/
- **Register Page**: http://127.0.0.1:8000/signup/
- **Login Page**: http://127.0.0.1:8000/login/
- **Forgot Password**: http://127.0.0.1:8000/forgot-password/

---

## 📝 **REGISTRATION GUIDE**

### **Option 1: Register as DONOR**

**Step 1: Go to Signup Page**

Click "Sign Up" on homepage or navigate to: http://127.0.0.1:8000/signup/

**Step 2: Fill Registration Form**

| Field | Example Value |
|-------|---|
| Username | donor_john |
| Email | donor@example.com |
| First Name | John |
| Last Name | Doe |
| Phone Number | 9876543210 |
| Password | SecurePass123! |
| Confirm Password | SecurePass123! |
| Role Selection | ◉ Medicine Donor |
| Organization Name | (Leave blank - optional) |

**Step 3: Submit Form**

- Click "Create Account" button
- You'll see: "Account created successfully. Please login."

**Step 4: Login**

- Go to: http://127.0.0.1:8000/login/
- Enter username: `donor_john`
- Enter password: `SecurePass123!`
- Click "Login"
- **Auto-redirect to**: Donor Dashboard

---

### **Option 2: Register as NGO/HOSPITAL**

**Step 1: Go to Signup Page**

Navigate to: http://127.0.0.1:8000/signup/

**Step 2: Fill Registration Form**

| Field | Example Value |
|-------|---|
| Username | ngo_lifecare |
| Email | ngo@lifecare.com |
| First Name | Life |
| Last Name | Care |
| Phone Number | 9876543210 |
| Password | SecurePass123! |
| Confirm Password | SecurePass123! |
| Role Selection | ◉ NGO/Hospital |
| Organization Name | Life Care Hospital |

**Step 3: Submit & Login**

- Same as donor
- **Auto-redirect to**: NGO Dashboard

---

### **Option 3: Register as DELIVERY BOY**

**Step 1: Go to Signup Page**

Navigate to: http://127.0.0.1:8000/signup/

**Step 2: Fill Registration Form**

| Field | Example Value |
|-------|---|
| Username | delivery_boy_1 |
| Email | deliveryboy@medshare.com |
| First Name | Raj |
| Last Name | Kumar |
| Phone Number | 9876543210 |
| Password | SecurePass123! |
| Confirm Password | SecurePass123! |
| Role Selection | ◉ Delivery Boy |
| Organization Name | (Leave blank) |

**Step 3: Admin Setup Required**

- Delivery boy account created but needs admin approval
- Admin must create DeliveryBoy profile with vehicle details
- Once approved, delivery boy can login and access dashboard

---

## 💚 **DONOR USER GUIDE**

### **After Login - Donor Dashboard**

**URL**: http://127.0.0.1:8000/donor/dashboard/

**Dashboard Shows**:

```
┌─────────────────────────────────────┐
│     MY DONATIONS DASHBOARD          │
├─────────────────────────────────────┤
│ [Total: 5] [Available: 3] [Donated: 2] │
├─────────────────────────────────────┤
│ ✅ List of all your medicine donations  │
│ 📊 Status of each medicine              │
│ 📅 Expiry dates                         │
└─────────────────────────────────────┘
```

---

### **Feature 1: Add New Medicine Donation**

**Step 1: Click "Add New Medicine" Button**

- On donor dashboard or go to: http://127.0.0.1:8000/add-medicine/

**Step 2: Fill Medicine Donation Form**

#### **BASIC INFORMATION**

| Field | Example |
|-------|---------|
| Medicine Name | Paracetamol |
| Brand Name | Calpol |
| Generic Name | Paracetamol |
| Category | Pain Reliever |
| Subcategory | Analgesics |

#### **DOSAGE DETAILS**

| Field | Example |
|-------|---------|
| Dosage Form | Tablet |
| Strength | 500mg |
| Composition | Paracetamol 500mg |
| Quantity | 50 |
| Unit | tablets |
| Batch Number | B123456 |
| Manufacturer | XYZ Pharma Ltd |
| Manufacture Date | 2024-01-01 |
| Expiry Date | 2026-12-31 (FUTURE DATE ONLY) |

#### **MEDICINE CONDITION**

| Field | Value |
|-------|-------|
| Condition | ◉ New/Sealed |
| Prescription Required | ☐ (check if needed) |

#### **STORAGE & USAGE**

| Field | Example |
|-------|---------|
| Storage Condition | Room temperature (15-30°C) |
| Usage Instructions | Take 1 tablet twice daily with water |
| Side Effects | May cause nausea in rare cases |
| Contraindications | Avoid if allergic to paracetamol |

#### **LOCATION DETAILS**

| Field | Example |
|-------|---------|
| Location Name | City Hospital Pharmacy |
| Latitude | 28.7041 |
| Longitude | 77.1025 |
| Pickup Available | ☑ (checked) |
| Delivery Available | ☑ (checked) |

#### **MEDICINE IMAGE**

| Field | Action |
|-------|--------|
| Upload Image | [Select file] |

**Step 3: Submit Form**

- Click "Add Medicine" button
- Success message: "Medicine listed for donation."
- Redirects to: Donor Dashboard

**Your Medicine Now**:
- ✅ Visible to all NGOs
- ✅ Searchable in medicine database
- ✅ Shown on medicine map
- ✅ Ready to receive requests

---

### **Feature 2: View Your Donations**

**On Donor Dashboard**, see:

```
For each medicine card:
┌──────────────────────────────────────┐
│  🖼️  [Medicine Image]                 │
│                                      │
│  💊 Paracetamol 500mg                │
│  📦 Quantity: 50 tablets             │
│  📅 Expires: Dec 31, 2026 (100 days) │
│  ⭐ Rating: 4.5/5 (8 reviews)       │
│  📍 Location: City Hospital Pharmacy │
│  🟢 Status: Available                │
│                                      │
│  [View Details] [Edit] [Delete]      │
└──────────────────────────────────────┘
```

**Statistics Shown**:
- Total Medicines: 5
- Available: 3
- Donated: 2

---

### **Feature 3: Edit Medicine Details**

**Click "Edit" on any medicine**

**Can Change**:
- Quantity (if not yet requested)
- Dosage details
- Location information
- Storage instructions
- Medicine image
- Description

**Cannot Change**:
- Medicine name (once published)
- Expiry date (should delete and re-add)

**Steps**:

1. Click "Edit" button
2. Modify fields
3. Click "Update Medicine"
4. Redirects to Dashboard

---

### **Feature 4: Delete Medicine**

**Click "Delete" on any medicine**

```
⚠️ Warning: "Delete this medicine? This cannot be undone."
```

- Click "OK" to confirm
- Medicine removed from system
- NGOs can no longer request it

---

### **Feature 5: Check Medicine Requests**

**From Navbar**:
- Click **"Dashboard"** or **"My Donations"**
- Scroll down to see medicine cards
- Each medicine shows requests

**For each medicine**:
- Count of pending requests
- Count of accepted requests
- Option to view all requests

**To view request details**:
- Click on medicine
- Go to: http://127.0.0.1:8000/medicine/{id}/
- See all NGO requests at bottom

---

### **Feature 6: Respond to NGO Requests**

**View Request Details**:
- Click on medicine → "View Details"
- Scroll to "Donation Requests" section

**For each request**:

```
Request from: ABC Hospital
Quantity Needed: 20 tablets
Status: Pending
Requested on: Jan 30, 2026

[✅ Accept] [❌ Reject]
```

**Accept Request**:

1. Click "Accept" button
2. Status changes to "Accepted"
3. NGO receives notification
4. Creates pickup/delivery record

**Reject Request**:

1. Click "Reject" button
2. Status changes to "Rejected"
3. NGO receives notification
4. Medicine remains available for others

---

### **Feature 7: Track Pickups & Deliveries**

**URL**: http://127.0.0.1:8000/pickup-delivery/dashboard/

**Shows**:

```
Your Pending Pickups:
┌─────────────────────────────────────┐
│ Medicine: Paracetamol 500mg         │
│ NGO: ABC Hospital                   │
│ Quantity: 20 tablets                │
│ Status: Pending Pickup              │
│ Scheduled: Feb 1, 2026              │
│                                     │
│ [View Details] [Mark Picked Up]     │
└─────────────────────────────────────┘
```

**Status Flow**:

1. **Pending** → Waiting for pickup
2. **Picked Up** → You delivered to delivery boy
3. **In Transit** → Delivery boy is delivering
4. **Delivered** → NGO received medicine

**Actions**:
- Click "View Details" → See full information
- Click "Mark Picked Up" → Confirm you gave it to delivery boy
- System auto-updates as delivery boy progresses

---

### **Feature 8: View Your Profile**

**URL**: http://127.0.0.1:8000/profile/

**Shows**:

```
YOUR PROFILE
─────────────────────────────────
Username: donor_john
Email: donor@example.com
Role: Medicine Donor
Phone: 9876543210
Location Coordinates:
  - Latitude: 28.7041
  - Longitude: 77.1025
Bio: (Optional)

DONATION STATISTICS
─────────────────────────────────
Total Medicines: 5
Active Medicines: 3
Medicines Donated: 2
Total Ratings Received: 8
```

**Edit Profile**:
- Click "Edit Profile"
- Update:
  - Phone number
  - Organization name
  - Latitude/Longitude
  - Bio/Description
  - Profile picture
- Click "Save" to update

---

### **Feature 9: Search & Browse Medicines**

**URL**: http://127.0.0.1:8000/search-medicines/

**Features**:
- Search by medicine name
- Filter by category
- Filter by minimum rating
- Filter by expiry (expiring soon)
- View all available medicines

**Use Cases**:
- Check what other donors have posted
- Research medicine availability
- See popular medicines
- Check ratings

---

### **Feature 10: View Medicine Map**

**URL**: http://127.0.0.1:8000/medicines-map/

**Features**:
- Interactive map showing all medicines
- Markers for each medicine location
- Click marker to see medicine details
- Zoom in/out to navigate
- See medicine quantity, expiry, rating
- Shows medicine pickup locations

---

### **Feature 11: Check Notifications**

**URL**: http://127.0.0.1:8000/notifications/

**Notification Types**:
- NGO requested your medicine
- Request accepted/rejected
- Medicine picked up
- Medicine in transit
- Medicine delivered

**Actions**:
- View all notifications
- Mark as read
- Click to see related medicine/request

---

### **Feature 12: Expiry Tracker**

**URL**: http://127.0.0.1:8000/expiry-tracker/

**Shows**:

```
EXPIRING VERY SOON (< 7 days)
┌──────────────────────────────┐
│ Paracetamol - Expires in 3 days
│ Ibuprofen - Expires in 5 days
└──────────────────────────────┘

EXPIRING SOON (< 30 days)
┌──────────────────────────────┐
│ Aspirin - Expires in 15 days
│ Vitamins - Expires in 20 days
└──────────────────────────────┘

NORMAL (> 30 days)
┌──────────────────────────────┐
│ Amoxicillin - Expires in 45 days
└──────────────────────────────┘

ALREADY EXPIRED
┌──────────────────────────────┐
│ (You should delete these)
└──────────────────────────────┘
```

---

### **Feature 13: Rate & Review Medicines**

**URL**: http://127.0.0.1:8000/medicine/{id}/rate/

**Steps**:

1. Click "Rate this medicine" on medicine detail page
2. Select rating: ⭐⭐⭐⭐⭐ (1-5 stars)
3. Write review (optional): "High quality, genuine product"
4. Click "Submit Review"

**Your rating visible to**:
- All NGOs viewing the medicine
- Influences other NGOs' decisions
- Affects medicine popularity

---

## 🏥 **NGO USER GUIDE**

### **After Login - NGO Dashboard**

**URL**: http://127.0.0.1:8000/ngo/dashboard/

**Dashboard Shows**:

```
┌──────────────────────────────────────┐
│    FIND MEDICINES DASHBOARD          │
├──────────────────────────────────────┤
│ [Pending Requests: 3] [Received: 5] │
├──────────────────────────────────────┤
│ ✅ Available medicines to request   │
│ 🤖 AI Recommendations for you       │
│ 📊 Filter and search options        │
└──────────────────────────────────────┘
```

---

### **Feature 1: Search Available Medicines**

**On NGO Dashboard**:

```
SEARCH FILTERS
─────────────────────────────────
Search by Name:    [___________]  🔍
Category:          [Select ▼]
Rating (min):      [Select ▼]
☐ Expiring Soon (within 30 days)

[Search] [Clear Filters]
```

**Results Show**:

```
For each medicine:
┌──────────────────────────────────┐
│  💊 Paracetamol 500mg            │
│  📍 City Hospital Pharmacy       │
│  ⭐ Rating: 4.5/5 (8 reviews)   │
│  📦 Qty: 50 tablets             │
│  📅 Expires: Dec 31, 2026       │
│  👤 Donor: Hospital A            │
│                                  │
│  [View Details] [Request]        │
└──────────────────────────────────┘
```

---

### **Feature 2: View Medicine Details**

**Click "View Details" on any medicine**

**Shows**:

```
MEDICINE INFORMATION
─────────────────────────────────
Name: Paracetamol 500mg
Generic: Paracetamol
Brand: Calpol
Category: Pain Reliever
Dosage: 500mg tablet

AVAILABILITY
─────────────────────────────────
Quantity: 50 tablets
Location: City Hospital Pharmacy
Latitude: 28.7041
Longitude: 77.1025
Pickup Available: ✅
Delivery Available: ✅

DONOR INFORMATION
─────────────────────────────────
Donor Name: John Doe
Donor Contact: 9876543210
Organization: (if any)

REVIEWS & RATINGS
─────────────────────────────────
Average Rating: 4.5/5
Review 1: "High quality medicine" - ⭐⭐⭐⭐⭐
Review 2: "Genuine product" - ⭐⭐⭐⭐
```

---

### **Feature 3: Request Medicine**

**Click "Request" button on medicine**

**Step 1: Fill Request Form**

```
Medicine Details (Auto-filled):
Name: Paracetamol 500mg
Donor: John Doe

YOUR REQUEST
─────────────────────────────────
Quantity Needed: [20] tablets
Message (Optional): We need this urgently for emergency cases.

[Submit Request]
```

**Step 2: Submit**
- Click "Submit Request"
- Message: "Request submitted successfully"
- Status: "Pending" (waiting for donor approval)

**Step 3: Wait for Donor Response**
- Donor receives notification
- Donor can Accept or Reject
- You receive notification of decision

---

### **Feature 4: Track Donation Requests**

**URL**: http://127.0.0.1:8000/donation-requests/

**Shows All Your Requests**:

```
PENDING REQUESTS (Waiting for donor approval)
┌──────────────────────────────────────┐
│ Paracetamol 500mg from John Doe      │
│ Quantity: 20 tablets                 │
│ Requested: Jan 30, 2026              │
│ Status: ⏳ Pending                   │
│                                      │
│ [View Details] [Cancel Request]      │
└──────────────────────────────────────┘

ACCEPTED REQUESTS (Ready for pickup)
┌──────────────────────────────────────┐
│ Ibuprofen 400mg from Jane Smith      │
│ Quantity: 30 tablets                 │
│ Status: ✅ Accepted                  │
│ Pickup Date: Feb 1, 2026             │
│                                      │
│ [View Details] [Track Delivery]      │
└──────────────────────────────────────┘

REJECTED REQUESTS
┌──────────────────────────────────────┐
│ Aspirin from Bob Wilson              │
│ Quantity: 15 tablets                 │
│ Status: ❌ Rejected                  │
│ Reason: (shown if provided)          │
│                                      │
│ [Search Alternative]                 │
└──────────────────────────────────────┘

COMPLETED REQUESTS
┌──────────────────────────────────────┐
│ Vitamins from ABC Hospital           │
│ Quantity: 40 capsules                │
│ Status: ✅ Completed                 │
│ Received: Jan 28, 2026               │
│                                      │
│ [Rate Donor] [Rate Delivery]         │
└──────────────────────────────────────┘
```

---

### **Feature 5: Track Deliveries**

**URL**: http://127.0.0.1:8000/pickup-delivery/dashboard/

**Shows Delivery Status**:

```
PENDING DELIVERY (Waiting to send pickup)
┌──────────────────────────────────────┐
│ Medicine: Paracetamol 500mg          │
│ Donor: John Doe                      │
│ Qty: 20 tablets                      │
│ Status: ⏳ Pending Pickup            │
│ Scheduled: Feb 1, 2026               │
└──────────────────────────────────────┘

IN TRANSIT (Being delivered to you)
┌──────────────────────────────────────┐
│ Medicine: Ibuprofen 400mg            │
│ Donor: Jane Smith                    │
│ Qty: 30 tablets                      │
│ Status: 🚚 In Transit                │
│ Delivery Boy: Raj Kumar              │
│ Delivery Boy Phone: 9876543210       │
│ Delivery Boy Location: On the way    │
│                                      │
│ [View on Map] [Track Live]           │
└──────────────────────────────────────┘

DELIVERED (Received)
┌──────────────────────────────────────┐
│ Medicine: Vitamins                   │
│ Donor: ABC Hospital                  │
│ Qty: 40 capsules                     │
│ Status: ✅ Delivered                 │
│ Delivered On: Jan 28, 2026           │
│ Received Quantity: 40 capsules       │
│                                      │
│ [View Receipt] [Confirm Receipt]     │
└──────────────────────────────────────┘
```

---

### **Feature 6: Confirm Medicine Receipt**

**When medicine arrives**:

**Step 1: Click "Confirm Receipt"**

```
DELIVERY CONFIRMATION
─────────────────────────────────
Medicine: Paracetamol 500mg
Expected Quantity: 50 tablets
Received Quantity: [50] tablets

Condition: ◉ Excellent
           ⭕ Good
           ⭕ Fair
           ⭕ Damaged

Notes: (optional)
_________________________

[Confirm Received] [Report Issue]
```

**Step 2: Confirm**
- Click "Confirm Received"
- Status changes to "Completed"
- Delivery boy gets notification
- System marks request as completed

---

### **Feature 7: Emergency Alerts**

**URL**: http://127.0.0.1:8000/emergency-alerts/

**Create Emergency Alert**:

**Step 1: Click "Create Alert"**

```
EMERGENCY REQUEST FORM
─────────────────────────────────
Medicine Needed: [Paracetamol____]
Category: [Pain Reliever ▼]
Quantity: [100] tablets
Priority: ◉ Critical
          ⭕ High
          ⭕ Medium
          ⭕ Low

Deadline: [Feb 1, 2026]
Patient Count: [50]
Description: Needed for accident victims at City Hospital
Location Name: City Hospital, Emergency Ward
Latitude: 28.7041
Longitude: 77.1025

[Create Alert]
```

**Step 2: Submit**
- Alert visible to all donors
- Marked as "URGENT"
- Auto-notifies nearby donors
- Donors can donate to fulfill urgent need

**View Alerts**:
- See all active emergency alerts
- See medicine needed
- See priority level
- See location
- Click to donate

---

### **Feature 8: Bulk Donation Requests**

**URL**: http://127.0.0.1:8000/bulk-requests/

**Create Bulk Request**:

```
BULK DONATION REQUEST
─────────────────────────────────
Title: Monthly Medicine Supply for Jan 2026
Description: We need regular medicines for our hospital...
Priority: High

ADD ITEMS
─────────────────────────────────
Item 1:
  Medicine: Paracetamol
  Category: Pain Reliever
  Quantity: 500
  Unit: Tablets
  [Add] [Remove]

Item 2:
  Medicine: Ibuprofen
  Category: Pain Reliever
  Quantity: 300
  Unit: Tablets
  [Add] [Remove]

[+ Add More Items] [Submit Request]
```

**Track Bulk Request**:
- View fulfillment progress
- See which items received
- See which items pending
- Estimated delivery dates

---

### **Feature 9: View Your Profile**

**URL**: http://127.0.0.1:8000/profile/

**Shows NGO Information**:

```
NGO PROFILE
─────────────────────────────────
Organization: Life Care Hospital
Username: ngo_lifecare
Email: ngo@lifecare.com
Phone: 9876543210
License Number: LIC123456
Location Coordinates:
  - Latitude: 28.7041
  - Longitude: 77.1025
Bio: "Serving community health needs"

NGO STATISTICS
─────────────────────────────────
Requests Made: 15
Requests Accepted: 12
Medicines Received: 12
Average Donor Rating: 4.8/5
```

**Edit Profile**:
- Click "Edit"
- Update phone, license, location, bio
- Upload organization logo/picture
- Save changes

---

### **Feature 10: Notifications**

**URL**: http://127.0.0.1:8000/notifications/

**Types of Notifications**:

```
1. REQUEST ACCEPTED
   ✅ Your request for Paracetamol from John Doe has been accepted.
   [View Details]

2. REQUEST REJECTED
   ❌ Your request for Aspirin from Bob Wilson has been rejected.
   [Request Different Medicine]

3. MEDICINE PICKED UP
   🚚 Paracetamol is on the way to you!
   Delivery boy: Raj Kumar
   [Track Delivery]

4. MEDICINE IN TRANSIT
   🚚 Your medicine is in transit.
   ETA: 2:00 PM
   [View Map]

5. MEDICINE DELIVERED
   📦 Your medicine has been delivered!
   [Confirm Receipt] [Rate Donor]

6. NEW EMERGENCY ALERT
   🚨 Critical: Paracetamol needed urgently
   [View Alert]
```

---

### **Feature 11: Inventory Tracking**

**Track medicine inventory**:
- System tracks quantities you've received
- Shows current stock levels
- Alerts when stock is low
- Helps plan future requests

---

## 🚚 **DELIVERY BOY USER GUIDE**

### **After Registration - Admin Setup**

**Important**: Your account needs admin approval first.

**What Admin Does**:
- Creates your DeliveryBoy profile
- Adds vehicle details
- Sets your initial location
- Marks you as available

**Once Approved**: You can login

---

### **After Login - Delivery Boy Dashboard**

**URL**: http://127.0.0.1:8000/delivery/dashboard/

**Dashboard Shows**:

```
┌──────────────────────────────────────────┐
│    MY DELIVERIES DASHBOARD               │
├──────────────────────────────────────────┤
│ Active: 3  Completed: 12  Total: 15     │
│ Rating: 4.8/5  Completion Rate: 98%     │
├──────────────────────────────────────────┤
│ ✅ Your assigned deliveries             │
│ 📍 Nearby available pickups              │
│ 🗺️ Real-time tracking map               │
└──────────────────────────────────────────┘
```

---

### **Feature 1: View Assigned Deliveries**

**Shows All Your Deliveries**:

```
ACTIVE DELIVERIES
┌──────────────────────────────────────────┐
│ Delivery #001                            │
│ Medicine: Paracetamol 500mg              │
│ From: John Doe (Donor)                   │
│ To: Life Care Hospital (NGO)             │
│ Quantity: 50 tablets                     │
│ Status: 🟡 Assigned                      │
│ Pickup Location: 28.7041, 77.1025        │
│ Delivery Location: 28.6139, 77.2090      │
│ Assigned: Jan 30, 2026, 10:00 AM         │
│                                          │
│ [View Details] [Start Pickup]            │
└──────────────────────────────────────────┘

COMPLETED DELIVERIES
┌──────────────────────────────────────────┐
│ Delivery #001 (Completed Jan 28)         │
│ Medicine: Ibuprofen 400mg                │
│ From: Jane Smith → ABC Hospital          │
│ Qty: 30 tablets                          │
│ Status: ✅ Delivered                     │
│ Delivered Time: 2:30 PM                  │
│ Rating: ⭐⭐⭐⭐⭐ 5/5                  │
│                                          │
│ [View Details]                           │
└──────────────────────────────────────────┘
```

---

### **Feature 2: Accept Delivery Assignment**

**When delivery is assigned to you**:

**Notification**: "New delivery assigned to you"

**Click "Start Pickup"**:

```
DELIVERY ACCEPTANCE
─────────────────────────────────
Delivery ID: #001
Medicine: Paracetamol
From: John Doe
Quantity: 50 tablets

Are you available to pick up this delivery?

[✅ Accept Delivery] [❌ Decline]
```

**After Accepting**:
- Status: "Assigned" → "Accepted"
- You can now start pickup
- GPS coordinates saved
- System locks delivery (no other boy can accept)

**If You Decline**:
- Admin assigns to another delivery boy
- You remain available for other deliveries

---

### **Feature 3: Mark as Picked Up**

**Step 1: Go to delivery location**

**Using GPS**:
- Your phone location auto-detected
- Navigate to donor's location
- See distance, estimated time on map

**Step 2: Click "Mark Picked Up"**

```
PICKUP CONFIRMATION
─────────────────────────────────
Delivery #001
Medicine: Paracetamol 500mg
Expected Qty: 50 tablets
Actual Qty Received: [50] tablets

Condition: ◉ Excellent
           ⭕ Good
           ⭕ Fair

Pickup Notes: Sealed properly, Temperature maintained
_________________________________________

[Confirm Pickup] [Report Issue]
```

**Step 3: Confirm**
- Click "Confirm Pickup"
- Photo/proof captured (if enabled)
- Status: "Picked Up"
- NGO receives notification: "Medicine picked up"
- Donor receives notification: "Medicine picked up"

---

### **Feature 4: Mark as In Transit**

**After pickup confirmed**:

**Click "Start Transit"**:

```
TRANSIT STARTED
─────────────────────────────────
Delivery #001 is now in transit
Estimated Delivery Time: 2:30 PM
Distance to Destination: 5.2 km
Route: Navigate to hospital

[Navigate] [Update Location] [Issues]
```

**Features During Transit**:
- Your GPS location auto-updated
- NGO can track you live on map
- You get turn-by-turn navigation
- Emergency call button to NGO

---

### **Feature 5: Mark as Delivered**

**When you reach NGO location**:

**Click "Mark Delivered"**:

```
DELIVERY CONFIRMATION
─────────────────────────────────
Delivery #001
Medicine: Paracetamol 500mg
Scheduled Qty: 50 tablets
Actual Delivered: [50] tablets

Delivered At: 14:30 (2:30 PM)
Delivery Location Confirmed: ✅
Receipt Signed By: [________]
Receiver Contact: [9876543210]

Condition Notes: 
_________________________________________

[Confirm Delivery]
```

**After Confirmation**:
- Status: "Delivered" ✅
- NGO receives: "Medicine delivered"
- NGO can confirm receipt
- Delivery marked complete
- Rating system opens

---

### **Feature 6: View Delivery Details**

**Click on any delivery**:

**Shows**:

```
DELIVERY DETAILS
─────────────────────────────────
Delivery ID: #001
Medicine: Paracetamol 500mg
Quantity: 50 tablets

PICKUP DETAILS
─────────────────────────────────
Donor: John Doe
Address: City Hospital Pharmacy
Phone: 9876543210
Pickup Time Slot: 10:00 AM - 1:00 PM
Coordinates: 28.7041, 77.1025

DELIVERY DETAILS
─────────────────────────────────
NGO/Hospital: Life Care Hospital
Address: Main Road Hospital
Contact: 9876543210
Expected Delivery: 2:00 PM - 4:00 PM
Coordinates: 28.6139, 77.2090

TRACKING HISTORY
─────────────────────────────────
✅ Assigned: Jan 30, 10:00 AM
✅ Picked Up: Jan 30, 11:30 AM
✅ In Transit: Jan 30, 11:45 AM
✅ Delivered: Jan 30, 2:30 PM

[Navigate to Pickup] [Navigate to Delivery]
```

---

### **Feature 7: Live Location Tracking**

**URL**: http://127.0.0.1:8000/delivery/map/

**Features**:

```
DELIVERY MAP
─────────────────────────────────
🟢 Your Location (Green dot)
🔴 Pickup Location (Red marker)
🟠 NGO Location (Orange marker)
🛣️ Suggested Route (Blue line)

Stats:
- Distance to Pickup: 5.2 km
- Distance to NGO: 3.4 km
- ETA to Pickup: 15 minutes
- ETA to NGO: 45 minutes
```

**Auto-Update**:
- Your location updated every minute
- NGO can see your location live
- Accuracy: ±20 meters

---

### **Feature 8: Nearby Available Pickups**

**Dashboard shows**:
- Pickups within 10 km
- Medicine name
- Pickup location
- Donor contact

**Click "Claim Delivery"**:
- Request to be assigned
- Admin confirms
- You become the assigned delivery boy

---

### **Feature 9: View Your Profile**

**URL**: http://127.0.0.1:8000/profile/

**Shows**:

```
DELIVERY BOY PROFILE
─────────────────────────────────
Name: Raj Kumar
Phone: 9876543210
Vehicle Type: Motorcycle
Vehicle Registration: DL-01-AB-1234
Current Status: 🟢 Available
Rating: 4.8/5 (45 deliveries rated)

DELIVERY STATISTICS
─────────────────────────────────
Total Deliveries: 45
Completed Deliveries: 44
Completion Rate: 97.8%
Average Rating: 4.8/5
```

**Edit Profile**:
- Update vehicle information
- Update phone number
- Update availability status

---

### **Feature 10: Update Availability Status**

**Click "Update Status"**:

```
AVAILABILITY STATUS
─────────────────────────────────
Current: 🟢 Available

Change to:
⭕ Available - Ready to accept deliveries
⭕ Busy - Already on delivery
⭕ Offline - Not available

[Update Status]
```

**What it Does**:
- **Available**: Admin can assign you deliveries
- **Busy**: Won't receive new assignments
- **Offline**: Hidden from assignment system

---

### **Feature 11: Notifications**

**Types**:

```
1. NEW DELIVERY ASSIGNED
   New delivery from John Doe to Life Care Hospital
   [Accept] [Decline]

2. PICKUP CONFIRMED
   NGO confirmed medicine received
   [View Rating]

3. DELIVERY RATING RECEIVED
   You received ⭐⭐⭐⭐⭐ 5/5 from ABC Hospital
   "Very professional and on time"

4. NEARBY PICKUP AVAILABLE
   Ibuprofen available for pickup nearby (2 km away)
   [View Details]
```

---

### **Feature 12: Daily Earnings/Statistics**

**Shows**:
- Deliveries completed today: 5
- Estimated earnings: $50
- Average delivery time: 35 minutes
- Customer rating: 4.9/5

---

## 👨‍💼 **ADMIN USER GUIDE**

### **Admin Login**

**URL**: http://127.0.0.1:8000/admin/

```
Username: admin  (or superuser account)
Password: (your admin password)
```

---

### **Feature 1: View Dashboard**

**URL**: http://127.0.0.1:8000/admin-reports/

**Shows**:

```
ADMIN DASHBOARD
─────────────────────────────────
MEDICINES
  Total: 150
  Available: 120
  Donated: 25
  Expired: 5

USERS
  Donors: 45
  NGOs: 18
  Delivery Boys: 12
  Total: 75

REQUESTS
  Total: 80
  Pending: 5
  Completed: 70

TOP MEDICINES (by rating)
  1. Paracetamol - ⭐⭐⭐⭐⭐ 4.9/5
  2. Ibuprofen - ⭐⭐⭐⭐ 4.7/5
  3. Vitamins - ⭐⭐⭐⭐ 4.6/5
```

---

### **Feature 2: Advanced Reports**

**URL**: http://127.0.0.1:8000/admin/reports/advanced/

**Features**:
- Monthly donation trends
- NGO performance statistics
- Donor statistics
- Delivery boy performance
- Medicine category breakdown
- Export all data as CSV

---

### **Feature 3: Export Data**

**Click "Export as CSV"**:

```
Downloads: medshare_reports.csv

Contains:
- Summary statistics
- All donation requests
- Donor information
- NGO information
- Medicine inventory
- Delivery history
```

**Use in Excel/Google Sheets**:
- Analyze trends
- Create reports
- Make strategic decisions

---

### **Feature 4: Manage Users**

**URL**: http://127.0.0.1:8000/admin/

**View All Users**:
- Click "Users" in Django admin
- See all registered accounts
- View role, email, phone
- See registration date

**Edit User**:
- Click on username
- Change password
- Toggle active status
- Change email
- Save changes

**Block User** (Deactivate):
- Click on username
- Uncheck "Active" checkbox
- Save
- User cannot login

**Delete User**:
- Click on username
- Click "Delete"
- Confirm deletion

---

### **Feature 5: Manage Delivery Boys**

**URL**: http://127.0.0.1:8000/admin/

**For Delivery Boy Account**:
- Click "Delivery Boys"
- View all registered delivery boys
- Click on delivery boy
- Fill form:

```
User: (select registered user)
Phone: 9876543210
Vehicle Type: Motorcycle
Vehicle Registration: DL-01-AB-1234
Is Available: Checked
Current Latitude: 28.7041
Current Longitude: 77.1025
Total Deliveries: 0
Completed Deliveries: 0
Rating: 0.0
Verified: Unchecked (check after verification)
```

- Save

**Approve Delivery Boy**:
- Fill all details
- Check "Verified" checkbox
- Save
- Delivery boy can now login and accept deliveries

---

### **Feature 6: View Medicines**

**URL**: http://127.0.0.1:8000/admin/

**Click "Medicines"**:
- See all medicines
- Filter by donor
- Filter by status
- View expiry dates
- Check ratings

**Edit Medicine**:
- Can change status
- Can mark as expired
- Can verify medicine
- Can delete if needed

---

### **Feature 7: Monitor Donations**

**URL**: http://127.0.0.1:8000/admin/

**Click "Donation Requests"**:
- See all requests
- View status (pending, accepted, rejected, completed)
- See request history
- Filter by date range

---

### **Feature 8: View Reports**

**Generate Reports**:

```
1. Monthly Donations Report
2. Donor Performance Report
3. NGO Performance Report
4. Delivery Boy Performance Report
5. Medicine Inventory Report
6. Expired Medicines Report
```

---

### **Feature 9: System Settings**

**Database Maintenance**:
- Run expire medicines command:

```bash
python manage.py expire_medicines
```

- This marks expired medicines daily
- Sends notifications to donors

---

## 📋 **COMMON TASKS SUMMARY**

### **Donor Checklist**

- ✅ Register as Donor
- ✅ Add medicines
- ✅ Receive NGO requests
- ✅ Accept/Reject requests
- ✅ Track pickups
- ✅ View ratings/reviews
- ✅ Check expiry tracker
- ✅ Manage profile

---

### **NGO Checklist**

- ✅ Register as NGO
- ✅ Search medicines
- ✅ Request medicines
- ✅ Track deliveries
- ✅ Confirm receipt
- ✅ Create emergency alerts
- ✅ Create bulk requests
- ✅ Rate donors/delivery boys

---

### **Delivery Boy Checklist**

- ✅ Register as delivery boy
- ✅ Wait for admin approval
- ✅ Accept assigned deliveries
- ✅ Pickup from donor
- ✅ Navigate to NGO
- ✅ Deliver to NGO
- ✅ Track performance
- ✅ Receive ratings

---

### **Admin Checklist**

- ✅ Manage all users
- ✅ Approve delivery boys
- ✅ Block fake users
- ✅ View reports
- ✅ Export data
- ✅ Monitor system
- ✅ Run maintenance commands

---

## 🎯 **QUICK REFERENCE LINKS**

### **GENERAL**

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| About | http://127.0.0.1:8000/about/ |
| FAQ | http://127.0.0.1:8000/faq/ |
| Contact | http://127.0.0.1:8000/contact/ |

### **AUTHENTICATION**

| Page | URL |
|------|-----|
| Register | http://127.0.0.1:8000/signup/ |
| Login | http://127.0.0.1:8000/login/ |
| Forgot Password | http://127.0.0.1:8000/forgot-password/ |
| Profile | http://127.0.0.1:8000/profile/ |

### **DONOR**

| Page | URL |
|------|-----|
| Dashboard | http://127.0.0.1:8000/donor/dashboard/ |
| Add Medicine | http://127.0.0.1:8000/add-medicine/ |
| Pickups | http://127.0.0.1:8000/pickup-delivery/dashboard/ |

### **NGO**

| Page | URL |
|------|-----|
| Dashboard | http://127.0.0.1:8000/ngo/dashboard/ |
| Emergency Alerts | http://127.0.0.1:8000/emergency-alerts/ |
| Bulk Requests | http://127.0.0.1:8000/bulk-requests/ |

### **DELIVERY BOY**

| Page | URL |
|------|-----|
| Dashboard | http://127.0.0.1:8000/delivery/dashboard/ |

### **COMMON**

| Page | URL |
|------|-----|
| Search | http://127.0.0.1:8000/search-medicines/ |
| Map | http://127.0.0.1:8000/medicines-map/ |
| Notifications | http://127.0.0.1:8000/notifications/ |
| Expiry Tracker | http://127.0.0.1:8000/expiry-tracker/ |

### **ADMIN**

| Page | URL |
|------|-----|
| Dashboard | http://127.0.0.1:8000/admin-reports/ |
| Advanced Reports | http://127.0.0.1:8000/admin/reports/advanced/ |
| Export CSV | http://127.0.0.1:8000/export-reports/ |
| Django Admin | http://127.0.0.1:8000/admin/ |

---

## 🛠️ **TROUBLESHOOTING**

### **Issue: Server won't start**

**Solution**:

```bash
# Make sure you're in the right directory
cd d:\Downloads\Medshare

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Try running migrations first
python manage.py migrate

# Then start server
python manage.py runserver
```

---

### **Issue: "Port 8000 already in use"**

**Solution**:

```bash
# Use a different port
python manage.py runserver 8001

# Or kill the process on port 8000
netstat -ano | findstr :8000  # Find process ID
taskkill /PID <ProcessID> /F   # Kill it
```

---

### **Issue: Can't login**

**Check**:
- Username and password are correct
- Account is active (not blocked by admin)
- User registered successfully

**If password forgot**:
- Use "Forgot Password" link
- Email will be sent to console (in development mode)
- Check terminal for reset link

---

### **Issue: Can't add medicine**

**Check**:
- You're logged in as Donor
- Expiry date is in the future
- All required fields filled
- Image file size is reasonable

---

### **Issue: Delivery boy can't login**

**Check**:
- Account registered
- Admin created DeliveryBoy profile
- Admin checked "Verified" checkbox
- Account is active

---

### **Issue: Can't see medicines on map**

**Check**:
- Medicines must have latitude and longitude
- Medicines must have status='available'
- Reload the page (F5)
- Check browser console for errors

---

### **Issue: Email not working**

**Check**:
- In development mode: Check terminal for email output
- In production: SMTP credentials are correct
- Email backend is configured in settings.py

---

## ✅ **YOU'RE ALL SET!**

Now you know how to:
- Register as any role
- Use all features
- Track donations
- Manage deliveries
- Export reports
- And much more!

**Start using the platform now!** 🎉

---

**Document Version**: 1.0
**Last Updated**: January 31, 2026
**Platform**: MedShare v1.0
**Status**: Production Ready
