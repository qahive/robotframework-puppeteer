import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

with open("README.md", "r", encoding='utf-8') as fh:
    LONG_DESCRIPTION = fh.read()

# Get the version from the _version.py versioneer file. For a git checkout,
# this is computed based on the number of commits since the last tag.
from PuppeteerLibrary._version import get_versions
VERSION = str(get_versions()['version']).split('+')[0]
del get_versions

setup(
    name="robotframework-PuppeteerLibrary",
    version=VERSION,
    author="QA Hive Co.,Ltd",
    author_email="support@qahive.com",
    description="PuppeteerLibrary is a Web Testing library for Robot Framework.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license="Apache License 2.0",
    url='https://qahive.github.io/robotframework-puppeteer.github.io/',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Framework :: Robot Framework",
    ],
    keywords='robotframework puppeteer web-testing automation',
    platforms='any',
    install_requires=[
        'robotframework>=3.2.1',
        'pyppeteer>=0.2.2'
    ],
    # python_requires='>3.5',
    # test_suite='nose.collector',
    # tests_require=['nose', 'parameterized'],
    zip_safe=False,
)
