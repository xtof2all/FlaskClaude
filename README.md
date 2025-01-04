# FlaskClaude

A Flask application with OAuth implementation demonstrating secure web application development with Flask and Google OAuth.

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
- `SESSION_COOKIE_HTTPONLY`: HTTP-only cookies (recommend: True)
- `REMEMBER_COOKIE_SECURE`: Secure remember cookies (True for HTTPS only)
- `REMEMBER_COOKIE_HTTPONLY`: HTTP-only remember cookies (recommend: True)

#### SSL Configuration (Production)
For HTTPS in production:
- `SSL_CERT`: Path to SSL certificate
- `SSL_KEY`: Path to SSL private key