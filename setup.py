#!/usr/bin/env python3

from setuptools import setup


setup(
    name = 'plover_spanish_mqd',
    version = '0.0.0',
    description = 'Support for plover in Spanish',
    long_description = file: README.md,
    author = 'Noelia Ruiz',
    author_email = 'nrm1977@gmail.com',
    license =  'GNU General Public License v2 or later (GPLv2+)',
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords = plover plover_plugin
    install_requires = [
        'plover>=4.0.0.dev0',
        'plover-python-dictionary>=0.5.9',
    ],
    packages = [
        'plover_spanish_mqd',
    ],
    entry_points = '''

    [plover.system]
    Spanish MQD = plover_spanish_mqd.system

    ''',
    include_package_data = True,
    zip_safe = True,
)
