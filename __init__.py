"""
FlaskClaude - A Flask application demonstrating OAuth implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A secure web application using Flask and Google OAuth, demonstrating:
    - Flask application factory pattern
    - Google OAuth integration
    - SQLAlchemy database management
    - Flask-Login user session management
    - Blueprint-based modular design

Basic usage:
    >>> from flask_claude import create_app
    >>> app = create_app()
    >>> app.run()

:copyright: (c) 2025 by xtof2all.
:license: MIT, see LICENSE for more details.
"""

__title__ = 'FlaskClaude'
__version__ = '0.1.0'
__author__ = 'xtof2all'
__license__ = 'MIT'
__copyright__ = '2025 xtof2all'

# Import version info for easier access
VERSION = __version__