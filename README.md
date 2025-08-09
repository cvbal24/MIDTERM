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