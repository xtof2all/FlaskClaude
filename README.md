# FlaskClaude

A Flask application with OAuth implementation demonstrating secure web application development with Flask and Google OAuth.

## Environment Configuration

The application uses environment variables for configuration. A template file `.env.example` is provided. To set up your environment:

1. Copy the example file:
```bash
cp .env.example .env
```

2. Configure the following variables in your `.env` file:

### Basic Flask Settings
- `FLASK_APP`: Entry point of the application (default: run.py)
- `FLASK_DEBUG`: Enable debug mode (True/False)
- `SECRET_KEY`: Security key for session management (change this!)

### Server Configuration
- `HOST`: Server host (default: 127.0.0.1)
- `PORT`: Server port (default: 5000)

### Database Settings
- `DATABASE_URL`: Database connection URL
  - Development (SQLite): `sqlite:///app.db`
  - Production (Example PostgreSQL): `postgresql://username:password@localhost:5432/flask_claude`

### Google OAuth Configuration
- `GOOGLE_CLIENT_ID`: Your Google OAuth client ID
- `GOOGLE_CLIENT_SECRET`: Your Google OAuth client secret
  - Obtain these from [Google Cloud Console](https://console.cloud.google.com)
  - Required scopes: email, profile

### Security Settings (Production)
- `SESSION_COOKIE_SECURE`: Enable secure cookies (recommend: True)
- `SESSION_COOKIE_HTTPONLY`: HTTP-only cookies (recommend: True)
- `REMEMBER_COOKIE_SECURE`: Secure remember cookies (recommend: True)
- `REMEMBER_COOKIE_HTTPONLY`: HTTP-only remember cookies (recommend: True)

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

3. Install dependencies:
```bash
pip install -e .
```

4. Set up environment variables:
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

Visit http://localhost:5000 to access the application.

## Development

The application uses:
- Flask's factory pattern for scalability
- Blueprints for modular organization
- SQLAlchemy ORM for database operations
- Flask-Login for session management
- Flask-Migrate for database migrations
- Google OAuth for authentication

## Database Management

The project includes database migrations:
```bash
# Apply migrations
flask db upgrade

# Create a new migration after model changes
flask db migrate -m "Description of changes"

# Rollback last migration
flask db downgrade
```

## Testing

Run the test suite:
```bash
python -m pytest
```

## Production Deployment

1. Update your `.env`:
```env
FLASK_DEBUG=False
DATABASE_URL=your-production-db-url
SECRET_KEY=your-secure-secret-key
SESSION_COOKIE_SECURE=True
```

2. Additional steps:
   - Set up HTTPS (required for OAuth)
   - Update Google OAuth redirect URIs
   - Use a production WSGI server (e.g., gunicorn)
   - Configure proper logging
   - Set up monitoring

## Contributing

1. Fork the repository
2. Create your feature branch
3. Write and test your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.