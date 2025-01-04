import re
from setuptools import setup, find_packages

# Read version from __init__.py
with open('__init__.py', 'r', encoding='utf-8') as f:
    version = re.search(r"__version__ = '(.+)'", f.read()).group(1)

# Read README for long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='FlaskClaude',
    version=version,
    author='xtof2all',
    author_email='',  # Add your email if you want to distribute the package
    description='A Flask application with OAuth implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xtof2all/FlaskClaude',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=[
        'Flask==3.0.0',
        'Flask-SQLAlchemy==3.1.1',
        'Flask-Login==0.6.3',
        'Flask-Migrate==4.0.5',
        'Flask-OAuthlib==0.9.6',
        'python-dotenv==1.0.0',
        'SQLAlchemy==2.0.25',
        'requests==2.31.0',
        'email-validator==2.1.0.post1',
        'rauth==0.7.3',
        'psycopg2-binary==2.9.9;platform_system!="Windows"',  # PostgreSQL driver
        'gunicorn==21.2.0;platform_system!="Windows"',  # Production server
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.3',
            'pytest-cov>=4.1.0',
            'flake8>=6.1.0',
            'black>=23.12.1',
            'mypy>=1.8.0',
        ],
        'prod': [
            'psycopg2-binary>=2.9.9',
            'gunicorn>=21.2.0',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Security',
    ],
    entry_points={
        'console_scripts': [
            'flask-claude=run:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/xtof2all/FlaskClaude/issues',
        'Source': 'https://github.com/xtof2all/FlaskClaude',
    },
)