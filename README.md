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

[Previous environment configuration content...]

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

[Rest of previous README content...]

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
SECRET_KEY=your-secure-secret-key
SESSION_COOKIE_SECURE=True  # Only if using HTTPS
```

[Rest of deployment instructions...]

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

[Previous license and contribution content...]