import os
from flask import Flask
from config import DevConfig, ProdConfig
from app.assets import assets

conf = {
    'development': DevConfig,
    'production': ProdConfig
}[os.environ.get('FLASK_ENV', 'development').lower()]

app = Flask(__name__)
app.config.from_object(conf)
assets.init_app(app)

from app import views  # noqa: E402, F401
