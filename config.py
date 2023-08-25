
class Config():
    pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:joan50%401$23@localhost/pythonchronicles'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
configu = {
    'development': DevelopmentConfig
}