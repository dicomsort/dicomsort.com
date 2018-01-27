import os
from flask import Flask
from config import DevConfig, ProdConfig

conf = {
    'development': DevConfig,
    'production': ProdConfig
}[os.environ.get('FLASK_ENV', 'development').lower()]

app = Flask(__name__)
app.config.from_object(conf)

from app import views
