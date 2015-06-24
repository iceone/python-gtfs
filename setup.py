
from setuptools import setup, find_packages


requires = [
    'iso639>=0.1.1',
    'language-tags>=0.3.2',
    'pycountry>=1.12',
    'pytz>=2015.4'
]

dependency = [
]

setup(
    name='GTFS',
    version='0.0.1a',
    description='gtfs python implementation.',
    long_description=(
        'Python implementation of '
        'General Transit Feed Specification'
    )
    license='MIT',
    author='Ilya A. Barsukov',
    author_email='ilya.a.barsukov@gmail.com',
    url='http://smart-transport.ru/',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            # not implemented
        ],
    },
    zip_safe=False,
    install_requires=requires,
    dependency_links=dependency
)
