# FlaskClaude

A simple Flask application with OAuth implementation. This project demonstrates how to build a secure web application using Flask and Google OAuth.

## Project Structure
```
FlaskClaude/
├── app/                      # Application package
│   ├── __init__.py          # App factory, extension initialization
│   ├── auth/                # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── oauth.py         # OAuth implementation
│   │   └── views.py         # Auth routes
│   ├── main/                # Main blueprint
│   │   ├── __init__.py
│   │   └── views.py         # Main routes
│   ├── models.py            # Database models
│   ├── static/              # Static files
│   └── templates/           # Jinja2 templates
│       ├── auth/
│       │   └── login.html
│       ├── errors/
│       │   └── 403.html
│       ├── base.html
│       ├── dashboard.html
│       └── index.html
├── migrations/              # Database migrations
├── tests/                   # Test suite
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore file
├── config.py               # Configuration classes
├── README.md               # This file
├── requirements.txt        # Project dependencies
├── run.py                  # Application entry point
└── setup.py               # Package setup file
```

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/xtof2all/FlaskClaude.git
cd FlaskClaude
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. Set up the environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
flask db upgrade
```

6. Run the application:
```bash
python run.py
```

The application will be available at http://localhost:5000

## Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the OAuth consent screen:
   - Go to "APIs & Services" > "OAuth consent screen"
   - Choose "External" user type
   - Fill in the application name and required fields
   - Add the following scopes:
     - .../auth/userinfo.email
     - .../auth/userinfo.profile

4. Create OAuth 2.0 credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Web application"
   - Add authorized redirect URIs:
     - http://localhost:5000/callback/google (development)
     - https://your-domain.com/callback/google (production)
   - Save your Client ID and Client Secret

5. Update your .env file:
```env
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
SECRET_KEY=your-secret-key
FLASK_DEBUG=True
```

## Development

- The application uses Flask's factory pattern
- Blueprints for modularity
- SQLAlchemy for ORM
- Flask-Login for session management
- Flask-Migrate for database migrations

## Testing

Run the test suite:
```bash
python -m pytest
```

## Production Deployment

1. Update .env:
```env
FLASK_DEBUG=False
DATABASE_URL=your-production-db-url
SECRET_KEY=your-secure-secret-key
```

2. Set up HTTPS (required for OAuth)
3. Update Google OAuth redirect URIs
4. Use a production WSGI server (e.g., gunicorn)
5. Set up proper monitoring and logging

## Contributing

1. Fork the repository
2. Create your feature branch
3. Write and test your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.