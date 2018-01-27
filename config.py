import os

class Config:

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    WEBROOT = os.path.join(BASEDIR, 'app')
    VERSION = '2.1.9'

    FREEZER_DEFAULT_MIMETYPE = 'text/html'
    FREEZER_DESTINATION = os.path.join(BASEDIR, 'build')

    GA_PROPERTY_ID = ''


class DevConfig(Config):

    DEBUG = True


class ProdConfig(Config):

    SERVER_NAME = 'dicomsort.com'
    PREFERRED_URL_SCHEME = 'https'

    FREEZER_BASE_URL = "%s://%s" % (PREFERRED_URL_SCHEME, SERVER_NAME)

    GA_PROPERTY_ID = 'UA-37902466-4'
