#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['snakebids==0.2.1' ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Ali Khan",
    author_email='alik@robarts.ca',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Snakebids Boilerplate contains all the boilerplate you need to create a Snakebids App.",
    entry_points={
        'console_scripts': [
            'snakebids_boilerplate=snakebids_boilerplate.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='snakebids_boilerplate',
    name='snakebids_boilerplate',
    packages=find_packages(include=['snakebids_boilerplate', 'snakebids_boilerplate.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/akhanf/snakebids_boilerplate',
    version='0.1.0',
    zip_safe=False,
)
