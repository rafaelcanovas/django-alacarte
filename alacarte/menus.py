from django.core.urlresolvers import reverse, NoReverseMatch


class Menu:
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
