# *HabitSync*

## Unit 4 Project - Django CRUD App
## Overview
This project is a Django-based web application implementing full CRUD functionality. It utilizes Django templates for rendering, PostgreSQL as the database, and Django's built-in authentication system. The app ensures that only authenticated users can create, update, or delete data.

## Features
- Full CRUD operations for managing data
- PostgreSQL database integration
- Responsive UI with CSS Flexbox/Grid for layout
- Deployed online for public access

## Getting Started
- **Deployed App:**


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
5. Create a .env file with your environment variables (see .env.example)
6. Run database migrations:
   ```bash
   python manage.py migrate
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Heroku Deployment
1. Create a Heroku account and install the Heroku CLI
2. Log in to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
4. Add PostgreSQL addon:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```
5. Configure environment variables:
   ```bash
   heroku config:set SECRET_KEY=your_secret_key
   heroku config:set DEBUG=False
   ```
6. Deploy to Heroku:
   ```bash
   git push heroku main
   ```
7. Run migrations on Heroku:
   ```bash
   heroku run python manage.py migrate
   ```
8. Create a superuser on Heroku (optional):
   ```bash
   heroku run python manage.py createsuperuser
   ```

## *Technologies Used*
- Django
- PostgreSQL
- HTML, CSS (Flexbox & Grid)
- Python
- Heroku (Deployment)
- Whitenoise (Static Files)

## Next Steps
- Implement additional features such as user profiles
- Improve UI/UX design
