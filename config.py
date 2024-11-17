# config.py
import os
API_KEY = "pub_58668d7976d1e378b598e5c485232fac693c6"
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///newsarc.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
    API_KEY = "pub_58668d7976d1e378b598e5c485232fac693c6"