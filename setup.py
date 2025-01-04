from setuptools import setup, find_packages

setup(
    name='FlaskClaude',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
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
        'rauth==0.7.3'
    ],
    python_requires='>=3.8',
)