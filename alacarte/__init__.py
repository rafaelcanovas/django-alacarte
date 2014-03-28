__title__ = 'alacarte'
__version__ = '0.1.2'
__author__ = 'Rafael Canovas'

from collections import defaultdict

from django.conf import settings
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule

from alacarte.menus import Menu

MENU_REGISTRY = defaultdict(list)


def register(menu_class):
	# Instantiate the menu class before registering it
	menu = menu_class()

	try:
		group = menu.group
	except AttributeError:
		group = ''

	MENU_REGISTRY[group].append(menu)


def get_menus(group):
	return MENU_REGISTRY[group]


def autodiscover():
	"""
	Discover and load menu.py files from all INSTALLED_APPS.
	Heavily inspired by django.contrib.admin.autodiscover
	"""

	for app in settings.INSTALLED_APPS:
		mod = import_module(app)
		try:
			import_module('%s.menu' % app)
		except:
			if module_has_submodule(mod, 'menu'):
				raise
