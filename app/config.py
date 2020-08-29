from dotenv import load_dotenv
import os

load_dotenv()
basedir =  os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY_DUMMY'
    SERVICENOW_SECRET = os.environ.get('SERVICENOW_SECRET') or 'TEST_PASSWORD'
    SERVICENOW_URL=os.environ.get('SERVICENOW_URL') or 'TEST_URL'
    SERVICENOW_USERNAME=os.environ.get('SERVICENOW_USERNAME') or 'TEST_USER'
    SERVICENOW_ASSIGNMENT_GROUP=os.environ.get('SERVICENOW_ASSIGNMENT_GROUP') or 'TEST GROUP'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SERVICENOW_CALLER_ID = os.environ.get('SERVICENOW_CALLER_ID') or 'TEST_USER'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
     