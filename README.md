# FlaskClaude

A simple Flask application with OAuth implementation. This project demonstrates how to build a secure web application using:

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
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.