from django.core.urlresolvers import reverse, NoReverseMatch


class Menu:
	submenus = ()

	def shown(self):
		"""
		All menus are shown by default.
		Override this method to implement custom behavior.
		"""
		return True

	def url(self):
		"""
		Try to reverse `url_name`, fallback to '#' if not possible.
		"""
		try:
			return reverse(self.url_name)
		except AttributeError:
			return '#'
		except NoReverseMatch:
			raise

	def is_active(self):
		"""
		A menu is active either if its `url_name` is the current or if
		any of its `submenus` are active.
		"""
		url = sub_urls = False
		if hasattr(self, 'url_name'):
			url = reverse(self.url_name) == self.context['request'].path
		if hasattr(self, 'submenus'):
			sub_urls = any([s.is_active() for s in self.submenus])

		return url or sub_urls
