import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Common config
    """


class DevelopmentConfig(Config):
    """
    dev config
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = '13264238467dshgjdsghfjsdjf'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../../db/temp_db')


class TestConfig(Config):
    """
    dev config
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = '13264238467dshgjdsghfjsdjf'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../../db/test.db')


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}
