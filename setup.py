#!/usr/bin/env python

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

try:
	import pypandoc
	readme = pypandoc.convert('README.md', 'rst')
except (ImportError, OSError, IOError):
	readme = ''

setup(
	name='django-alacarte',
	version='0.1.4',
	description='A minimalist Django menu app.',
	long_description=readme,
	author='Rafael Canovas',
	author_email='rafaelcanovas@me.com',
	url='https://github.com/mstrcnvs/django-alacarte',
	include_package_data=True,
	packages=[
		'alacarte',
		'alacarte.templatetags'
	],
	install_requires=[
		'Django'
	],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Utilities'
	]
)
