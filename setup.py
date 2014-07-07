import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()

requires = [
    'paste',
    'pyramid',
    'pyramid_mako',
    'waitress',
    'gevent',
    'gevent-socketio',
    ]

setup(name='team-v',
      version='0.0',
      description='team-v',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='team-v.herokuapp.com',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="teamv",
      entry_points="""\
      [paste.app_factory]
      main = teamv:main
      """,
      )
