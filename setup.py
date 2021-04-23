#!/usr/bin/env python3

from setuptools import setup


setup(
	name='plover_spanish_mqd',
	version='2.0.1',
	description='Support for plover in Spanish (Melany system)',
	long_description='file: README.md',
	url='https://github.com/nvdaes/plover_spanish_mqd',
	author='Noelia Ruiz',
	author_email='nrm1977@gmail.com',
	license='GNU General Public License v3 or later (GPLv3+)',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Plugins',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.8',
	],
	keywords='plover plover_plugin',
	install_requires=[
		'plover>=4.0.0.dev8',
		'plover-python-dictionary>=1,<2',
		'plover-start-words>=1,<2',
	],
	extras_require={
		'test': '''
		plover==4.0.0.dev9
		pytest
	'''
	},
	packages=[
		'plover_spanish_mqd',
	],
	entry_points='''

	[plover.system]
	Spanish MQD = plover_spanish_mqd.system
	''',
	include_package_data=True,
	zip_safe=True,
)
