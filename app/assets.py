from flask_assets import Bundle, Environment

css = Bundle(
    'css/suever.css',
    filters='cssmin',
    output='css/common.css'
)

assets = Environment()
assets.register('css', css)
