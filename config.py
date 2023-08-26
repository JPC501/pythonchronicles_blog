from datetime import timedelta

class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:joan50%401$23@localhost/pythonchronicles'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)
    
class DevelopmentConfig(Config):
    DEBUG = True
    
    
configu = {
    'development': DevelopmentConfig
}