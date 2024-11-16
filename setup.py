import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'SPOCK',
    version = '2.0',
    author = 'Elsa Ducrot',
    author_email = 'ducrotelsa@gmail.com',
    description = ('Speculoos Observatory SChedule maKer for chilean night on SPECULOOS South Observatory'),
    keywords = '',
    url = 'https://github.com/educrot22/SPOCK/',
    packages = find_packages(),
    long_description = read('README.rst'),
    python_requires='>=3.6',
)
