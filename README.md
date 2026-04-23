# Quietude Stories - Full-Stack Editorial Sanctuary

Quietude Stories is a premium, long-form storytelling platform designed for intentional reading and writing. It features a modern, editorial design with a robust Python/Flask backend.

## 🚀 Features

- **Editorial Sanctuary**: A beautifully designed homepage featuring trending stories.
- **Dynamic Story Feed**: A live feed that fetches stories directly from the database.
- **Story Editor**: A dedicated space for writers to compose and publish their narratives.
- **Bookstore**: A curated collection of physical volumes and journals.
- **Authentication**: Secure Login and Sign-up system using JWT tokens.
- **Author Profiles**: Personalized spaces for storytellers to showcase their work.

## 🛠️ Tech Stack

- **Frontend**: HTML5, Tailwind CSS (via CDN), JavaScript (Fetch API).
- **Backend**: Python, Flask, Flask-SQLAlchemy (ORM), Flask-JWT-Extended (Auth).
- **Database**: SQLite (Local development).

## 📦 Project Structure

```text
writersspot/
├── backend/
│   ├── app.py             # Main Flask application & API routes
│   ├── models.py          # Database schema (User, Story, Book)
│   ├── init_db.py         # Database initialization & seeding script
│   ├── requirements.txt   # Python dependencies
│   └── quietude.db        # SQLite database file
└── frontend/
    ├── api.js             # Centralized API utility for the frontend
    ├── homepage/          # Main landing page
    ├── story_feed/        # Dynamic feed of stories
    ├── story_editor/      # Interface to write and publish stories
    ├── book_store/        # Bookstore and journal shop
    └── login_sign_up/     # Authentication pages
```

## ⚙️ Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Shivachetla/writespot.git
cd writespot
```

### 2. Set Up the Backend
It is recommended to use a virtual environment:
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Initialize the Database
Run the seeding script to set up sample users and stories:
```bash
python init_db.py
```

### 4. Run the Application
Start the Flask server:
```bash
python app.py
```
The backend will be running at `http://127.0.0.1:5000`.

### 5. Open the Frontend
Simply open `frontend/homepage/code.html` in your favorite web browser.

## 📝 Test Account
You can login with the pre-seeded account:
- **Email**: `elara@quietude.com` (Username: `elara`)
- **Password**: `password123`

## 📄 License
This project is for educational purposes as part of the "WritersSpot" initiative.
