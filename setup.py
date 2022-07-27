#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["aiohttp","requests","lru-dict"]

test_requirements = ['pytest>=3',
                     'requests-mock',
                     'aioresponses',
                     'pytest-asyncio',
                     'nox']

setup(
    author="SpeakinTelnet",
    author_email='gui.lac@protonmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description="A python api wrapper to access the available enpoints from the blockscan.com ecosystem",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords='blockscan-python',
    name='blockscan-python',
    packages=find_packages(include=['blockscan*'],
                           exclude=['docs', 'tests', 'test_data']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SpeakinTelnet/blockscan-python',
    version='1.1.1',
    zip_safe=False,
)
