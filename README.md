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
=======
- Flask web framework
- Google OAuth authentication
- SQLAlchemy database integration
- Modern Python practices
- Clean architecture principles

## Project Setup

### 1. Clone and Install Dependencies
```bash
git clone https://github.com/xtof2all/FlaskClaude.git
cd FlaskClaude
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Google OAuth Configuration

#### Setting up Google OAuth 2.0:
1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Navigate to "APIs & Services" > "Credentials"
4. Click "Create Credentials" and select "OAuth client ID"
5. Configure the OAuth consent screen if not already done:
   - Add your app name
   - Add your development email
   - For testing, you can keep it in "Testing" status
6. Create OAuth client ID:
   - Select "Web application" as application type
   - Add a name for your OAuth client
   - Add authorized redirect URIs:
     - For development: `http://localhost:5000/callback/google`
     - For production: `https://yourdomain.com/callback/google`
7. Copy your Client ID and Client Secret

#### Configure the Application:
1. Create a .env file from the template:
```bash
cp .env.example .env
```

2. Update the .env file with your Google credentials:
```env
GOOGLE_CLIENT_ID=your-client-id-here
GOOGLE_CLIENT_SECRET=your-client-secret-here
SECRET_KEY=your-secret-key-here
```

### 3. Database Setup
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Run the Application
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
=======
The application will be available at `http://localhost:5000`

## Features

- **Google OAuth Login**: Secure authentication using Google OAuth 2.0
- **User Management**: Automatic user creation on first login
- **Profile Dashboard**: Display user information from Google profile
- **Database Integration**: Support for SQLite (development) and other SQL databases (production)
- **Responsive UI**: Bootstrap-based interface
- **Flash Messages**: User feedback system
- **Protected Routes**: @login_required decorator for secure access

## Development

- The application uses Flask blueprints for modularity
- OAuth implementation is extensible for adding other providers
- Environment-based configuration for development and production
- SQLAlchemy ORM for database interactions

## Production Deployment

For production deployment:
1. Update .env with production database URL and credentials
2. Set FLASK_ENV=production
3. Configure a proper web server (e.g., Gunicorn)
4. Set up HTTPS (required for OAuth)
5. Update OAuth redirect URIs in Google Console


## Contributing

1. Fork the repository
2. Create your feature branch
3. Write and test your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
=======
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

