# FlaskClaude

A Flask application with OAuth implementation demonstrating secure web application development with Flask and Google OAuth.

## Installation Options

FlaskClaude can be installed with different configurations depending on your needs:

### Basic Installation
For basic development setup:
```bash
git clone https://github.com/xtof2all/FlaskClaude.git
cd FlaskClaude
pip install -e .
```

### Development Installation
Includes testing and code quality tools:
```bash
pip install -e .[dev]
```
This adds:
- pytest for testing
- pytest-cov for coverage reports
- flake8 for code linting
- black for code formatting
- mypy for type checking

### Production Installation
Includes production server and database drivers:
```bash
pip install -e .[prod]
```
This adds:
- psycopg2-binary for PostgreSQL support
- gunicorn for production server

## Environment Configuration

The application uses environment variables for configuration. A template file `.env.example` is provided. To set up your environment:

1. Copy the example file:
```bash
cp .env.example .env
```

2. Configure the following variables in your `.env` file:

### Required Settings

#### Basic Flask Settings
- `FLASK_APP`: Entry point of the application (default: run.py)
- `FLASK_ENV`: Application environment ('development' or 'production')
- `FLASK_DEBUG`: Enable debug mode (True/False, disable in production)
- `SECRET_KEY`: Security key for session management (use a strong random key)

#### Database Settings
- `DATABASE_URL`: Database connection URL
  - Development (SQLite): `sqlite:///app.db`
  - Production (PostgreSQL example): `postgresql://username:password@localhost:5432/flask_claude`
  - For PostgreSQL, install additional dependency: `pip install psycopg2-binary`

#### Google OAuth Configuration
- `GOOGLE_CLIENT_ID`: Your Google OAuth client ID
- `GOOGLE_CLIENT_SECRET`: Your Google OAuth client secret
  - Obtain these from [Google Cloud Console](https://console.cloud.google.com)
  - Required scopes: email, profile
  - Set up authorized redirect URIs:
    - Development: http://localhost:5000/callback/google
    - Production: https://your-domain.com/callback/google

### Optional Settings

#### Server Configuration
- `HOST`: Server host (default: 127.0.0.1)
  - Use 0.0.0.0 to accept all incoming connections
- `PORT`: Server port (default: 5000)

#### Security Settings (Production)
These settings require HTTPS in production:
- `SESSION_COOKIE_SECURE`: Enable secure cookies (True for HTTPS only)
  - Ensures cookies are only sent over HTTPS
  - Must be False if not using HTTPS
- `SESSION_COOKIE_HTTPONLY`: HTTP-only cookies (recommend: True)
  - Prevents JavaScript access to cookies
  - Protects against XSS attacks
- `REMEMBER_COOKIE_SECURE`: Secure remember cookies (True for HTTPS only)
  - Similar to SESSION_COOKIE_SECURE but for "remember me" functionality
- `REMEMBER_COOKIE_HTTPONLY`: HTTP-only remember cookies (recommend: True)
  - Similar to SESSION_COOKIE_HTTPONLY but for "remember me" functionality

#### SSL Configuration (Production)
For HTTPS in production:
- `SSL_CERT`: Path to SSL certificate
- `SSL_KEY`: Path to SSL private key

## Project Structure
[Previous project structure section...]

## Development

### Code Quality
With the development installation, you can use:
```bash
# Run tests
pytest

# Check code coverage
pytest --cov=app

# Format code
black .

# Check types
mypy .

# Lint code
flake8
```

### Package Version
Current version: 0.1.0 (from __init__.py)

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

## Production Deployment

1. Install with production dependencies:
```bash
pip install -e .[prod]
```

2. Update your `.env`:
```env
FLASK_ENV=production
FLASK_DEBUG=False
DATABASE_URL=your-production-db-url
SECRET_KEY=your-secure-secret-key  # Use a strong random key
SESSION_COOKIE_SECURE=True  # Only if using HTTPS
SESSION_COOKIE_HTTPONLY=True
REMEMBER_COOKIE_SECURE=True  # Only if using HTTPS
REMEMBER_COOKIE_HTTPONLY=True
```

3. Set up HTTPS (required for OAuth):
   - Obtain SSL certificate (e.g., Let's Encrypt)
   - Configure SSL in your web server
   - Update SSL_CERT and SSL_KEY in .env

4. Database Setup:
   - For PostgreSQL:
     ```bash
     pip install psycopg2-binary
     ```
   - Create database and user
   - Update DATABASE_URL in .env
   - Run migrations: `flask db upgrade`

5. Web Server Setup:
   - Install and configure Gunicorn:
     ```bash
     pip install gunicorn
     gunicorn -w 4 -b 127.0.0.1:8000 run:app
     ```
   - Set up Nginx as reverse proxy
   - Configure systemd service

6. Google OAuth Setup:
   - Update authorized redirect URIs in Google Console
   - Add your production domain
   - Update OAuth credentials in .env

7. Security Considerations:
   - Enable all secure cookie settings
   - Configure HTTPS properly
   - Set up proper CSP headers
   - Regular security updates
   - Monitoring for unusual activities

## Package Information

- Version: 0.1.0
- Python Support: 3.8+
- License: MIT
- Author: xtof2all

## Command Line Usage

After installation, you can run the application using:
```bash
# Using the entry point
flask-claude

# Or traditional Flask way
flask run
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Write and test your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.