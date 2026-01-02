import os

class Config:
    """Base configuration class. Handles database connection settings."""
    SQLALCHEMY_DATABASE_URI = os.environ.get ('DATABASE_URL')

    #Disable tracking modifications for better performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
