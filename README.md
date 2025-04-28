# Blog Application Backend (Python Flask)

## Overview
A backend-only blog application developed with Python Flask.  
The system allows users to create blog posts, manage email subscribers, and automatically notify subscribers when a new post is published.

No frontend is included — the project is focused purely on backend API functionality.

## Key Features
- Blog post creation and listing via API.
- Email subscription management.
- Automated email notifications when new articles are posted.
- SQLite used for lightweight database management.

## Technologies Used
- Python 3
- Flask (Backend Framework)
- SQLite (Database)
- SMTP (Python Standard Library for Email)

## API Endpoints
- `POST /create-post` → Create a new blog post.
- `GET /posts` → Fetch all blog posts.
- `POST /subscribe` → Subscribe a new user to receive email notifications.

## How to Run Locally
1. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows
    ```
2. Install dependencies:
    ```bash
    pip install flask
    ```
3. Navigate to the `fikrlog/` directory and run the Flask app:
    ```bash
    python app.py
    ```
4. Access the API at: `http://localhost:5000/`

## Future Improvements
- Implement user authentication and admin dashboard.
- Develop a simple frontend to interact with APIs.
- Deploy the backend using Render, Railway, or AWS.

## Author
Mahmudjonov Zohidjon  
(Seoul, South Korea)
