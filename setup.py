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
	version='0.1.1',
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
		'Framework :: Django',
		'Programming Language :: Python',
		'Programming Language :: Python 3'
	]
)
