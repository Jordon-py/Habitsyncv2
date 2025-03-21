# *HabitSync*

## Unit 4 Project - Django CRUD App
## Overview
This project is a Django-based web application implementing full CRUD functionality. It utilizes Django templates for rendering, PostgreSQL as the database, and Django's built-in authentication system. The app ensures that only authenticated users can create, update, or delete data.

## Features
- Full CRUD operations for managing habits
- User authentication and authorization
- PostgreSQL database integration
- Responsive UI with CSS Flexbox/Grid for layout
- Deployed online for public access

## Getting Started
- **Deployed App:** https://habitsync-4c41c4781ea2.herokuapp.com/

### Installation (For Local Development)
1. Clone the repository:
   ```bash
   git clone https://github.com/Jordon-py/Unit4-Project.git
   ```
2. Navigate into the project folder:
   ```bash
   cd Unit4-Project
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a .env file with your environment variables (copy from .env.example):
   ```
   SECRET_KEY=your_secure_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   USE_HTTPS=False
   # Leave DATABASE_URL empty to use SQLite for local development
   ```
6. For PostgreSQL (optional), create a database and add to .env:
   ```
   DATABASE_URL=postgres://user:password@localhost:5432/habitsync_db
   ```
7. Run database migrations:
   ```bash
   python manage.py migrate
   ```
8. Start the development server:
   ```bash
   python manage.py runserver
   ```
9. Visit http://localhost:8000 in your browser

### Running on HTTP vs HTTPS
- For local development, HTTP is the default (USE_HTTPS=False)
- For production with HTTPS, set USE_HTTPS=True in environment variables
- When USE_HTTPS is False, secure cookies are disabled for HTTP compatibility

### GitHub and Heroku Deployment
1. Create a new GitHub repository and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/habitsync.git
   git push -u origin main
   ```
2. Create a Heroku account and install the Heroku CLI
3. Log in to Heroku:
   ```bash
   heroku login
   ```
4. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
5. Add PostgreSQL addon:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```
6. Configure environment variables:
   ```bash
   heroku config:set SECRET_KEY=your_secure_secret_key_here
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com,localhost,127.0.0.1
   # For HTTPS (recommended in production):
   heroku config:set USE_HTTPS=True
   # For HTTP only (not recommended in production):
   heroku config:set USE_HTTPS=False
   ```
7. Deploy from GitHub:
   - Go to the Heroku Dashboard
   - Select your app
   - Go to the "Deploy" tab
   - Under "Deployment method", select "GitHub"
   - Connect to your GitHub repository
   - Enable automatic deploys or manually deploy your main branch
8. Alternatively, deploy directly from git:
   ```bash
   git push heroku main
   ```
9. Run migrations on Heroku:
   ```bash
   heroku run python manage.py migrate
   ```
10. Create a superuser on Heroku (optional):
    ```bash
    heroku run python manage.py createsuperuser
    ```

## *Technologies Used*
- Django
- PostgreSQL (or SQLite for local development)
- HTML, CSS (Flexbox & Grid)
- Python
- Heroku (Deployment)
- Whitenoise (Static Files)
- GitHub (Version Control)

## Next Steps
- Implement habit streaks and statistics
- Add user profiles with customization options
- Create a mobile-responsive UI with dark/light themes
- Implement social sharing features
