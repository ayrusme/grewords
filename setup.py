import json
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = []
tests_require = []

with open('Pipfile.lock') as fd:
    lock_data = json.load(fd)
    install_requires = [
        package_name + package_data['version']
        for package_name, package_data in lock_data['default'].items()
    ]
    tests_require = [
        package_name + package_data['version']
        for package_name, package_data in lock_data['develop'].items()
    ]

setup(
    name='grewords',
    version='0.0.1',
    description='A project that helps you with GRE prep',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ayrusme/grewords',
    author='Surya Raman',
    author_email='hello@suryaraman.blog',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='gre wordlist',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.5',
    install_requires=install_requires,
    data_files=[('/usr/local/grewords/', ['grewords/words.csv'])],
    package_data = {
        '': ['*.csv'],
    },
    include_package_data = True,
    entry_points={
        'console_scripts': [
            'grewords=grewords.words:main',
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/ayrusme/grewords/issues',
        'Source': 'https://github.com/ayrusme/grewords',
    }
)
