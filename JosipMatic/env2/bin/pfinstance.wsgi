from os import environ
from pyramid.paster import get_app, setup_logging

environ['VIRTUAL_ENV'] = '/var/www/html/jmatic/env2
envitor['HGENCODING'] = 'utf-8'
ini_path = '/var/www/html/jmatic/CTA_project/cta_project/production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
