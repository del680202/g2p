# -*- coding: utf-8 -*-
"""
    g2p.py
    ~~~~~~~~
    
    HTTP Proxy Server in Python.
    
    :copyright: (c) 2015 by Terrence Chin.
    :license: BSD, see LICENSE for more details.
"""
from setuptools import setup

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Operating System :: MacOS',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: Microsoft',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: Proxy Servers',
    'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
]

setup(
    name                = 'g2p',
    version             = '0.1',
    description         = 'HTTP Proxy Server in Python, Convert GET to POST',
    long_description    = open('README.md').read().strip(),
    author              = 'Terrence Chin',
    author_email        = 'del680202@gmail.com',
    url                 = 'https://github.com/del680202/g2p',
    license             = 'BSD',
    packages            = ['g2p'],
    scripts             = ['g2p/g2p.py'],
    install_requires    = [],
    classifiers         = classifiers
)
