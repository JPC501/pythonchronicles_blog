from datetime import timedelta


class Config():
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://your-db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)
    CKEDITOR_PKG_TYPE = 'full'


class DevelopmentConfig(Config):
    DEBUG = True


configu = {
    'development': DevelopmentConfig
}
