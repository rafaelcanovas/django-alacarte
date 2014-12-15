__title__ = 'alacarte'
__version__ = '0.1.4'
__author__ = 'Rafael Canovas'

from collections import defaultdict

from django.conf import settings
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule

from alacarte.menus import Menu

MENU_REGISTRY = defaultdict(list)


def register(*menu_classes):
	"""
	Register one or more menu classes in the menu registry.
	"""
	for menu_class in menu_classes:
		# Instantiate the menu class before registering it
		menu = menu_class()

		try:
			group = menu.group
		except AttributeError:
			group = ''

		MENU_REGISTRY[group].append(menu)


def clear_registry():
	"""
	Clear alacarte's menu registry.
	Useful for testing.
	"""
	global MENU_REGISTRY
	MENU_REGISTRY.clear()


def get_menus(group):
	"""
	Get the group corresponding menus from the menu registry and order
	them using the 'order' attribute.
	"""
	menus = MENU_REGISTRY[group]
	menus = sorted(
		menus,
		key=lambda m: (hasattr(m, 'order'), getattr(m, 'order', None)),
		reverse=True
	)
	return menus


def autodiscover():
	"""
	Discover and load menu.py files from all INSTALLED_APPS.
	Heavily inspired by django.contrib.admin.autodiscover.
	"""
	for app in settings.INSTALLED_APPS:
		mod = import_module(app)
		try:
			import_module('%s.menu' % app)
		except:
			if module_has_submodule(mod, 'menu'):
				raise
