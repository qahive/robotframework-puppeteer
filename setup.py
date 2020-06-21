import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

with open("README.md", "r", encoding='utf-8') as fh:
    LONG_DESCRIPTION = fh.read()

with open(join(CURDIR, 'PuppeteerLibrary', '__init__.py'), encoding='utf-8') as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)


setup(
    name="robotframework-PuppeteerLibrary",
    version=VERSION,
    author="QA Hive Co.,Ltd",
    author_email="support@qahive.com",
    description="ExcelDataDriver is a Excel Data-Driven Testing library for Robot Framework.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license="Apache License 2.0",
    url='https://github.com/qahive/robotframework-puppeteer',
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
