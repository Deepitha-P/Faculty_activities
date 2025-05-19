# 🎓 Faculty Activities Management System

A web-based system designed for academic institutions to track and manage faculty activities. Faculty members can log their academic contributions such as workshops, seminars, and talks. Admins can view, filter, and export activity data based on academic year and type.

---

## 🔑 Key Features

### 👨‍🏫 Faculty Panel
- Login with credentials
- Add new entries:
  - SDP Attended
  - SDP Organised
  - Invited Talks
- View and manage activity history

### 👩‍💼 Admin Panel
- Admin login access
- View all faculty entries
- Filter by:
  - Faculty Name
  - Activity Type
  - Year
- Export filtered data to Excel

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite

---

## 🚀 How to Run the Project Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Deepitha-P/Faculty_activities.git
   cd faculty-activities
   python -m venv venv
   venv\Scripts\activate
   python manage.py migrate
   python manage.py runserver
   
