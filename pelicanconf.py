#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alexandros Kosiaris'
SITENAME = u'JAB: Just Another Blog'
SITEURL = 'http://blog.uname.gr'

PATH = 'content'

TIMEZONE = 'UTC'
THEME = 'themes/twitchy'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (
        ('github', 'http://github.com/akosiaris'),
        ('twitter', 'http://twitter.com/kosiaris'),
        )

DEFAULT_PAGINATION = 10

STATIC_PATHS = [ 'images', 'extra/CNAME', 'extra/googlebf3ef559c8fe5d4e',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/googlebf3ef559c8fe5d4e': { 'path': 'googlebf3ef559c8fe5d4e.html'},
}
LOCALE='C'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
