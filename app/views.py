import requests
from datetime import datetime

# Import Flask app
from app import app

# Flask imports
from flask import render_template, request, url_for


@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def index():
    description = 'DICOM Sort is a free and open-source program for ' \
                  'organizing and renaming DICOM image files'
    return render_template('index.html', description=description)


@app.route('/documentation.html')
def documentation():
    description = 'DICOM Sort is an easy to use and extremely flexible ' \
                  'DICOM sorting utility'
    return render_template(
                'documentation.html',
                title='Documentation',
                description=description,
            )


@app.route('/downloads.html')
def downloads():
    description = 'DICOM Sort offers compiled binaries for Mac and PC ' \
                  'as well as Python source code'
    return render_template(
                'downloads.html',
                title='Downloads',
                description=description,
                version=app.config['VERSION'],
            )


@app.route('/features.html')
def features():
    description = 'DICOM Sort supports both medical image sorting as well ' \
                  'as anonymization'
    return render_template(
                'features.html',
                title='Features',
                description=description,
            )


@app.route('/release.html')
def release():
    description = 'DICOM Sort has a quarterly release cycle to provide ' \
                  'new features and improvements'
    return render_template(
                'release.html',
                title='Release Notes',
                description=description,
            )


# Internal endpoint for checking the latest version
@app.route('/current')
def current():
    payload = {
        'v': 1,
        'tid': app.config['GA_PROPERTY_ID'],
        'cid': request.remote_addr,
        't': 'event',
        'ec': 'Update',
        'ea': 'Check'
    }

    requests.post('http://www.google-analytics.com/collect', data=payload)
    return app.config['VERSION']


# Special error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Search Engine and Google Webmaster tools configuration
@app.route('/robots.txt')
def robots():
    return "User-agent: *\nSitemap: %s" % url_for('sitemap', _external=True)


@app.route('/google732ee66856c8d2d9.html')
def google():
    return 'google-site-verification: google732ee66856c8d2d9.html'


@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')


@app.route('/privacy-policy.html')
def privacy_policy():
    description = 'Privacy Policy for DICOM Sort - How we collect, use, and protect your information'
    return render_template(
        'privacy-policy.html',
        title='Privacy Policy',
        description=description,
    )


@app.route('/terms-of-service.html')
def terms_of_service():
    description = 'Terms of Service for DICOM Sort - Rules and guidelines for using our website and software'
    return render_template(
        'terms-of-service.html',
        title='Terms of Service',
        description=description,
    )


@app.route('/cookie-policy.html')
def cookie_policy():
    description = 'Cookie Policy for DICOM Sort - How we use cookies and tracking technologies'
    return render_template(
        'cookie-policy.html',
        title='Cookie Policy',
        description=description,
    )
