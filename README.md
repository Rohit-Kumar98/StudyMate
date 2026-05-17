# StudyMate – Student Resource Sharing Platform

StudyMate is a Django-based academic resource sharing platform where students can upload notes, PYQs, quizzes, assignments, and other study materials, while administrators verify and approve resources before they become publicly available.

The platform creates a secure, organized, and verified environment for academic content sharing inside a college ecosystem.

It helps students access quality learning resources easily while ensuring only approved and useful materials are available on the platform.

---

## Features

### Authentication System
- Student Signup using College Registration Number
- Secure Login / Logout
- User-specific Dashboard Access

---

### Resource Management
- Upload Notes, PYQs, Quizzes, Assignments, and Lab Files
- Resource Detail Page
- View File and Download File functionality

---

### Admin Verification System
- Admin-only Pending Resources Panel
- Approve Resources before publishing
- Delete / Reject invalid uploads
- Role-based Access Control for staff/admin users

---

### Browse & Filter System
- Browse all approved resources
- Filter by:
  - Subject
  - Resource Type
  - Semester

---

### User Tracking System
- My Uploads Page
- Upload Status Tracking (Pending / Approved)

---

### Profile System
- User Profile Page
- Registration Number Display
- Upload Statistics:
  - Total Uploads
  - Approved Uploads
  - Pending Uploads

---

### Collaboration Features
- Comment Section for resource discussion and doubt-solving

---

### Professional UI
- Shared Base Layout using `base.html`
- External CSS Styling
- Navbar + Footer
- Card-based Responsive Layout
- Professional Dashboard Design

---

## Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite

### Authentication
- Django Built-in Authentication System

### File Handling
- Django Media Files

---

## Project Structure

```bash
studymate/
│
├── resources/
│   ├── migrations/
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── dashboard.html
│   │   ├── upload.html
│   │   ├── browse.html
│   │   ├── resource_detail.html
│   │   ├── my_uploads.html
│   │   ├── profile.html
│   │   └── pending_resources.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── media/
├── db.sqlite3
├── manage.py
└── studymate/
