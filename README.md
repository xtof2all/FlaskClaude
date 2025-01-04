# FlaskClaude

A Flask application with OAuth implementation demonstrating secure web application development with Flask and Google OAuth.

[Previous sections remain the same until Project Structure...]

## Project Structure

```
FlaskClaude/
├── app/                      # Application package
│   ├── __init__.py          # App factory, extension initialization
│   ├── auth/                # Authentication blueprint
│   │   ├── __init__.py      # Blueprint initialization
│   │   ├── oauth.py         # OAuth implementation classes
│   │   └── views.py         # Auth routes and handlers
│   ├── main/                # Main application blueprint
│   │   ├── __init__.py      # Blueprint initialization
│   │   └── views.py         # Main routes and views
│   ├── models.py            # Database models (User model)
│   ├── static/              # Static assets (CSS, JS, images)
│   └── templates/           # Jinja2 HTML templates
│       ├── auth/            # Authentication templates
│       │   └── login.html   # OAuth login page
│       ├── errors/          # Error page templates
│       │   └── 403.html     # Forbidden error page
│       ├── base.html        # Base template with common layout
│       ├── dashboard.html   # User dashboard template
│       └── index.html       # Homepage template
├── migrations/              # Database migrations
│   ├── versions/           # Migration version files
│   ├── alembic.ini         # Alembic configuration
│   ├── env.py              # Migration environment
│   └── script.py.mako      # Migration template
├── tests/                   # Test suite directory
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore patterns
├── __init__.py             # Package metadata and version
├── config.py               # Configuration classes
├── requirements.txt        # Project dependencies
├── run.py                  # Application entry point
└── setup.py               # Package setup configuration
```

### Component Details

#### Application Package (`app/`)
- `__init__.py`: Contains the application factory and initializes Flask extensions (SQLAlchemy, Login Manager)
- `models.py`: Defines the User model with OAuth-related fields and helper methods

#### Authentication (`app/auth/`)
- `oauth.py`: Implements OAuth providers and authentication logic
- `views.py`: Handles login/logout routes and OAuth callbacks
- `__init__.py`: Sets up the authentication Blueprint

#### Main Application (`app/main/`)
- `views.py`: Contains the main application routes (home, dashboard)
- `__init__.py`: Sets up the main application Blueprint

#### Templates (`app/templates/`)
- `base.html`: Base template with navigation and common structure
- `auth/`: Authentication-related templates
- `errors/`: Error pages (403, etc.)
- Dashboard and index pages

#### Database Management
- `migrations/`: Contains database schema versions
- Alembic configuration for Flask-Migrate
- Version files track schema changes

#### Configuration
- `.env.example`: Template for environment variables
- `config.py`: Configuration classes for different environments (development, production)
- `__init__.py`: Package version and metadata
- `setup.py`: Installation and dependency configuration

#### Entry Points
- `run.py`: Main application entry point
- Command-line interface integration

#### Development
- `tests/`: Test suite directory (unit tests, integration tests)
- Development tools configuration

### Key Design Patterns

1. **Blueprint Pattern**: Modular application structure with auth and main blueprints
2. **Factory Pattern**: Application factory in `app/__init__.py`
3. **MVC Pattern**: 
   - Models: `models.py`
   - Views: Blueprint view files
   - Templates: Jinja2 templates
4. **OAuth Integration**: Extensible OAuth provider system

[Rest of the README content remains the same...]