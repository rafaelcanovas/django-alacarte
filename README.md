Alacarte
========

`django-alacarte` is a minimalist menu app for Django.

## Installation

```bash
$ pip install django-alacarte
```

## Usage

Add "alacarte" to your INSTALLED_APPS:

```python
INSTALLED_APPS = (
	...,
	'alacarte',
)
```

Create a menu.py inside your app and register your menus:

```python
import alacarte


class BankTransactionsMenu(alacarte.Menu):
	label = 'Transactions'
	url_name = 'bank_transactions'


class BankBalanceMenu(alacarte.Menu):
	label = 'Balance'
	url_name = 'bank_balance'


class BankPremiumMenu(alacarte.Menu):
	label = 'Premium Offers'
	url_name = 'bank_premium_offers'

	def shown(self)
		user = self.context['user']
		return user.is_premium()


class BankMenu(alacarte.Menu):
	group = 'main'
	label = 'Bank'
	submenus = (
		BankTransactionsMenu,
		BankBalanceMenu,
		BankPremiumMenu,
	)

	def shown(self):
		user = self.context['user']
		return user.is_authenticated()


alacarte.register(BankMenu)
```

Then in your template:

```django
{# ... #}
	{# ... #}
	{% alacarte "main" %}
	{# ... #}
{# ... #}
```

-----

`django-alacarte` is not related to https://pypi.python.org/pypi/alacarte


