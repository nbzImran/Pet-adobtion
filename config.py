import os


# Basic confiquration
SQLALCHEMY_DATABASE_URI =  'sqlite:///adopt.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
DEBUG_TB_INTERCEPT_REDIRECTS = False  # For Debug Toolbar
