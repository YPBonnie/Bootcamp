# Twitter API Clone 🚀

A robust RESTful API backend built with **Python Flask** and **PostgreSQL**. This project simulates core social media functionalities, focusing on user management, tweet distribution, and a complex many-to-many relationship for "likes."

## 🛠 Tech Stack
* **Backend Framework**: Python Flask
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Containerization**: Docker & Docker Compose
* **Migrations**: Flask-Migrate (Alembic)
* **API Testing**: Insomnia

## ✨ Key Features
* **User CRUD**: Full implementation of Create, Read, Update, and Delete operations for user profiles.
* **Tweet Management**: Endpoints for users to create and manage their tweets.
* **Many-to-Many Relationships**: A junction table implementation allowing users to "like" multiple tweets and tweets to be liked by multiple users.
* **Schema Evolution**: Managed database migrations to ensure incremental and reversible structural changes.

## 📂 Project Structure
```text
.
├── migrations/         # Database version control files
├── src/
│   ├── api/
│   │   ├── users.py    # Business logic for user-related routes
│   │   └── tweets.py   # Business logic for tweet-related routes
│   └── models.py       # SQLAlchemy models (User, Tweet, likes_table)
├── docker-compose.yml  # Container orchestration
└── seed.py             # Script for database initialization
```
# Getting Started

## 1. Launch Environment
Sign up the PostgreSQL database container:

`docker-compose up -d`

## 2. Initialize Database
Run migrations and seed the database with initial data:

`flask db upgrade`

`python seed.py`

## 3. Run the Application
`flask run`

The API will be accessible at *http://localhost:5000*. 
