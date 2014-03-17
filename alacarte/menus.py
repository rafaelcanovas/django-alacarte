from django.core.urlresolvers import reverse, NoReverseMatch


class Menu:
	@classmethod
	def shown(cls):
		"""
		All menus are shown by default.
		Override this method to implement custom behavior.
		"""
		return True

	@classmethod
	def url(cls):
		"""
		Try to reverse `url_name`, fallback to '#' if not possible.
		"""
		try:
			return reverse(cls.url_name)
		except AttributeError:
			return '#'
		except NoReverseMatch:
			raise

	@classmethod
	def is_active(cls):
		"""
		A menu is active either if its `url_name` is the current or if
		any of its `submenus` are active.
		"""
		url = sub_urls = False
		if hasattr(cls, 'url_name'):
			url = reverse(cls.url_name) == cls.context['request'].path
		if hasattr(cls, 'submenus'):
			sub_urls = any([s.is_active() for s in cls.submenus])

		if url or sub_urls:
			print('%s is active' % cls.label)

		return url or sub_urls
