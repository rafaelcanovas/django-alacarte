from __future__ import absolute_import

from django import template
from django.template.loader import render_to_string

from alacarte import get_menus

register = template.Library()


class AlacarteNode(template.Node):
	def __init__(self, menus):
		self.menus = menus

	def render(self, context):
		# Feed them with the context!
		for m in self.menus:
			m.context = context
			for s in m.submenus:
				s.context = context

		return render_to_string('alacarte/menu.html', {
			'menus': self.menus
		}, context)


@register.tag
def alacarte(parser, token):
	try:
		tag, group = token.split_contents()
	except ValueError:
		group = '""'

	if not (group[0] == group[-1] and group[0] in ('"', "'")):
		raise template.TemplateSyntaxError(
			"%r tag's argument should be in quotes" % tag
		)

	return AlacarteNode(get_menus(group[1:-1]))
