This is a simple web application built with Django that mimics a basic Twitter-like functionality. Users can create and post tweets with optional image uploads, while a built-in content filter prevents the use of specific prohibited words. The application uses Django's built-in administrative panel for managing posts.

Features
Post Tweets: A user-friendly form to compose and post text-based tweets (up to 280 characters).

Image Uploads: Option to include an image with each tweet post.

Content Filtering: A server-side validation that prevents tweets containing a list of specified prohibited words ("shit", "fuck", "bobo").

Admin Management: All tweets can be viewed, edited, and deleted through the Django admin interface.

Setup Instructions
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You need the following software installed on your system:

Python 3.x: This project is built using Python.

Git: For cloning the repository.

Pip: Python's package installer.

1. Clone the Repository
Open your terminal or command prompt and run the following command to clone the project to your local machine.

git clone <your_repository_url>
cd act3


NOTE: Please replace <your_repository_url> with the actual URL of your Git repository (e.g., https://github.com/your-username/act3.git).

2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to isolate the project's dependencies from your global Python environment.

For Windows:

python -m venv .venv
.\.venv\Scripts\activate


For macOS / Linux:

python3 -m venv .venv
source ./.venv/bin/activate


3. Install Dependencies
With your virtual environment active, install all the necessary Python packages using the requirements.txt file.

pip install -r requirements.txt


4. Apply Database Migrations
Run the database migrations to set up the database tables for your models.

python manage.py makemigrations tweets
python manage.py migrate


5. Create a Superuser
To access the Django admin panel and manage the tweets, you must create a superuser account.

python manage.py createsuperuser


Follow the prompts to enter your desired username, email, and a secure password.

6. Run the Development Server
You are now ready to run the application.

python manage.py runserver


The application will be available at http://127.0.0.1:8000/.

How to Use the App
Posting a Tweet
Access the Form: Navigate to http://127.0.0.1:8000/tweets/post/ in your web browser.

Compose: Enter your tweet content in the "Tweet Content" text area.

Add Image: Optionally, click "Choose file" to select an image from your computer to accompany your tweet.

Post: Click the "Post" button to submit your tweet. If successful, you will see a success message.

Word Filtering: The app will block tweets containing specific words and display a validation error.

Managing Tweets in the Admin Panel
Go to Admin: Visit http://127.0.0.1:8000/admin/.

Log In: Use the superuser credentials you created in the setup process.

Manage: Once logged in, you can click on the "Tweets" model to view all posted tweets, and add, edit, or delete them as needed.

Project Structure
Activity/
├── .gitignore          # Files ignored by Git
├── README.md           # This file
├── manage.py           # Django's command-line utility
├── requirements.txt    # Project dependencies
├── Activity/               # The main Django project folder
│   ├── _init_.py
│   ├── asgi.py
│   ├── settings.py     # Project-level settings
│   ├── urls.py         # Project-level URL patterns
│   └── wsgi.py
└── tweets/             # The Django app for tweet functionality
    ├── _init_.py
    ├── admin.py
    ├── forms.py        # Tweet form with custom validation
    ├── models.py       # Tweet model for the database
    ├── urls.py         # App-level URL patterns
    ├── views.py        # App-level views for handling logic
    └── templates/
        └── tweets/

            └── ... (HTML templates)
