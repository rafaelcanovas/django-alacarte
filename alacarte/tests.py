#!/usr/bin/env python

import os
import unittest
import alacarte

BASE_DIR = os.path.realpath(os.path.dirname(__file__))

from django.conf import settings
if not settings.configured:
	settings.configure(
		TEMPLATE_DIRS=(os.path.join(BASE_DIR, 'templates'),)
	)

import django
if hasattr(django, 'setup'):
	django.setup()

from django.template.loader import render_to_string
from django.template import Context


class AlacartTestCase(unittest.TestCase):
	def setUp(self):
		"""
		Create sample menus for testing.
		"""
		class TestSubMenu(alacarte.Menu):
			label = 'test sub menu'

		class TestMenu(alacarte.Menu):
			group = 'test'
			label = 'test menu'
			submenus = (TestSubMenu(),)

		class TestMenu2(alacarte.Menu):
			group = 'test'
			label = 'test menu 2'

		self.test_menu = TestMenu
		self.test_menu_2 = TestMenu2

	def test_entry_points(self):
		alacarte.Menu
		alacarte.autodiscover
		alacarte.register

	def test_autodiscover(self):
		alacarte.autodiscover()

	def test_register(self):
		alacarte.clear_registry()
		alacarte.register(self.test_menu)
		self.assertEqual(len(alacarte.get_menus('test')), 1)

	def test_register_multiple(self):
		alacarte.clear_registry()
		alacarte.register(self.test_menu, self.test_menu_2)
		self.assertEqual(len(alacarte.get_menus('test')), 2)

	def test_render(self):
		c = Context({'menus': alacarte.get_menus('test')})
		t = render_to_string('alacarte/menu.html', c)
		print(t)
		self.assertNotEqual(len(t), 0)


if __name__ == '__main__':
	unittest.main()
