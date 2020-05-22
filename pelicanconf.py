#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Steve Hayes'
SITENAME = u'Curriculum Vitae'
SITEURL = ''
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

THEME = 'themes/Flex'

PLUGIN_PATHS = ['./pelican-plugins']

#---------------------------------------------------------
PLUGINS = ['sitemap', 'post_stats', 'feed_summary']
SITEURL = 'http://localhost:8000'
SITETITLE = 'Steve Hayes'  # Replace with your name
SITESUBTITLE = 'Thought creates...'
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Add a link to your social media accounts
SOCIAL = (
    ('github', 'https://github.com/steviehayes'),
    ('envelope', 'mailto:steve.j.hayes@gmail.com'),
    ('linkedin','https://www.linkedin.com/in/stevehayes/'),
    ('twitter','https://twitter.com/StePurpleHayes')
)

STATIC_PATHS = ['images', 'extra']

# Main Menu Items
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'))

#LINKS = (
 #   ("About", "about"),
  #  ("Contact", "contact"),
#)


# Code highlighting the theme
PYGMENTS_STYLE = 'friendly'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# HOME_HIDE_TAGS = True
FEED_USE_SUMMARY = True