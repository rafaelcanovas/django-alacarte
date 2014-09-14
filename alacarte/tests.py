#!/usr/bin/env python

import unittest
import alacarte

from django.conf import settings
settings.configure()


class AlacartTestCase(unittest.TestCase):
	def setUp(self):
		"""
		Create sample menus for testing.
		"""
		class TestMenu(alacarte.Menu):
			group = 'test'
			label = 'test menu'

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


if __name__ == '__main__':
	unittest.main()
