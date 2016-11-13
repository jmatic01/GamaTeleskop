import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = ['pyramid', 'WebError', 'pymongo' ,'pyramid_mako','pyramid_chameleon','pyramid_debugtoolbar','waitress']

setup(name='cta_project',
      version='0.0',
      description='cta_project',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="Josip Matić",
      author_email='jmatic01@fesb,hr',
      url='https://github.com/niallo/pyramid_mongodb',
      keywords='web pyramid pylons mongodb',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="cta_project",
      entry_points = """\
      [paste.app_factory]
      main = cta_project:main
      """,
      paster_plugins=['pyramid'],
      )

