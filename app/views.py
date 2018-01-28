import os
import requests

# Import Flask app
from app import app

# Flask imports
from flask import render_template, request, send_file, url_for, Response


@app.route('/')
def index():
    description = 'DICOMsort is a free and open-source program for organizing and renaming DICOM image files'
    return render_template('index.html', description=description)

@app.route('/documentation.html')
def documentation():
    description = 'DICOMsort is an easy to use and extremely flexible DICOM sorting utility'
    return render_template('documentation.html', title='Documentation', description=description)

@app.route('/downloads.html')
def downloads():
    description = 'DICOMsort offers compiled binaries for Mac and PC as well as Python source code'
    return render_template('downloads.html',
                           title='Downloads',
                           description=description,
                           version=app.config['VERSION'])

@app.route('/features.html')
def features():
    description = 'DICOMsort supports both medical image sorting as well as anonymization'
    return render_template('features.html', title='Features', description=description)

@app.route('/release.html')
def release():
    description = 'DICOMsort has a quarterly release cycle to provide new features and improvements'
    return render_template('release.html', title='Release Notes', description=description)

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
    r = requests.post('http://www.google-analytics.com/collect', data=payload)
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
