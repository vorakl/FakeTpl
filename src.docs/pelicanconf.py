#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### Basic configuration
########################

AUTHOR = u'Oleksii Tsvietnov'
SITENAME = u"FakeTpl"
SITEURL = 'http://faketpl.vorakl.name'
SITEDESC = u'A fake template engine for different Shells'
SITE_VERSION = '1492380984'
SITE_KEYWORDS = 'faketpl,template engine,template,shell template'
PATH = 'content' # the location of all content
ARTICLE_PATHS = ['articles'] # a place for articles under the content location
PAGE_PATHS = ['pages']
CONTACT_URL = 'http://vorakl.name/pages/about/'
START_URL = 'pages/info/' # What's a start point of a site (like 'news/' or 'pages/about/')?
TIMEZONE = 'Europe/Berlin'
THEME = "theme"
DEFAULT_LANG = u'en'
RELATIVE_URLS = True  # disable in public version
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
PLUGINS = ['minify'] # keep 'minify' plugin as the last element in the list to minify all output HTMLs

DEFAULT_PAGINATION = 10 # Turns on the pagination
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/p{number}/', '{base_name}/p{number}/index.html'),
)

DELETE_OUTPUT_DIRECTORY = True  # build an output dir from scratch every time
OUTPUT_RETENTION = [".git", "CNAME", "README.md", "faketpl", "faketpl.sha256"] # but these dirs and files should be kept


### Interface configuration
############################

DISPLAY_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ITEMS_ON_MENU = True # Items are set in the MENUITEMS variable below

DISPLAY_SIDEBAR = False
DISPLAY_ARCHIVES_ON_SIDEBAR = False # It also turns on/off an appropriate section in a sitemap.xml
DISPLAY_CATEGORIES_ON_SIDEBAR = False # It also turns on/off an appropriate section in a sitemap.xml
DISPLAY_TAGS_ON_SIDEBAR = False # It also turns on/off an appropriate section in a sitemap.xml
DISPLAY_PAGES_ON_SIDEBAR = True # It also turns on/off an appropriate section in a sitemap.xml
DISPLAY_AUTHORS_ON_SIDEBAR = False # It's turned off because I'm the only one author on this site
DISPLAY_SUBSCRIBES_ON_SIDEBAR = False
DISPLAY_SITE_ON_SIDEBAR = False
DISPLAY_LINKS_ON_SIDEBAR = False # Links are set in the LINKS variable below

MENUITEMS = [("download", "http://faketpl.vorakl.name/faketpl"),
             ("blog", "http://vorakl.name/"),
             ("author", "http://vorakl.name/pages/about/")
            ]
#LINKS = [("Github", "https://github.com/vorakl"), ("LinkedIn", "https://linkedin.com/in/vorakl/")]
DISPLAY_AUTHOR = False # Add an author in a article's metadata

CATEGORIES_DESCRIPTION = {}
TAGS_DESCRIPTION = {}

### Feed's specification 
#########################

FEED_EMAIL = None # disable in development version
FEED_DOMAIN = '' # and create all feed under the local domain for testing purpose
FEED_MAX_ITEMS = 15
FEED_ALL_ATOM = ''
FEED_ALL_RSS = None # Here is used the only one feed on Google's feedburner. All other feeds are disabled
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None


### Static files (non templates)
#################################

STATIC_PATHS = [
    'static/robots.txt', 
    'static/favicon.ico'
    ]
# and sprecial output paths for them
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'}
    }


### Templates for html pages
#############################

# blog posts related pages

# If there is a 'Save_as' metadata (like in 404.html), then a page will be rendered anyway
ARTICLE_SAVE_AS = '' # activates rendering each article
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_LANG_SAVE_AS = ''
ARTICLE_LANG_URL = '{category}/{slug}-{lang}/'
DRAFT_SAVE_AS = '' # activates rendering each article's draft
DRAFT_URL = 'drafts/{category}/{slug}/'
DRAFT_LANG_SAVE_AS = 'drafts/{category}/{slug}-{lang}/index.html'
DRAFT_LANG_URL = 'drafts/{category}/{slug}-{lang}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'  # activates rendering each page.
PAGE_URL = 'pages/{slug}/'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}/index.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}/'
CATEGORY_SAVE_AS = '' # activates rendering each category
CATEGORY_URL = 'category/{slug}/'
TAG_SAVE_AS = '' # activates rendering each tag
TAG_URL = 'tag/{slug}/'
AUTHOR_SAVE_AS = '' # activates rendering each author
AUTHOR_URL = 'author/{slug}/'

# site related pages

# a list of templates for rendering blog posts. Not all of them, just an index and groups of entities (tags, categories, ...)
# other templates for blog posts rendering (for a tag, a category, ...) are activated by *_SAVE_AS variables below
DIRECT_TEMPLATES = []
PAGINATED_DIRECT_TEMPLATES = []

INDEX_SAVE_AS = 'news/index.html'
AUTHORS_SAVE_AS = 'author/index.html'  # defines where to save an authors page, it's activated by DIRECT_TEMPLATES 
AUTHORS_URL = 'author/'
ARCHIVES_SAVE_AS = 'archives/index.html' # defines where to save an archives page, it's activated by DIRECT_TEMPLATES 
ARCHIVES_URL = 'archives/'
TAGS_SAVE_AS = 'tag/index.html' # defines where to save a tags page, it's activated by DIRECT_TEMPLATES
TAGS_URL = 'tag/'
CATEGORIES_URL = 'category/' # defines where to save a categories page, it's activated by DIRECT_TEMPLATES
CATEGORIES_SAVE_AS = 'category/index.html'
PAGES_SAVE_AS = 'pages/index.html' # defines where to save a list of all pages, it's activated by TEMPLATE_PAGES
PAGES_URL = 'pages/'

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html' # activates rendering an archive page per year/month/day
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = ''

# additional pages

# a hash array with an extra list of 'templates+output_filename' for rendering besides of blog posts
# The output filename is needed because they don't have *_SAVE_AS variables
TEMPLATE_PAGES = {'sitemap.html': 'sitemap.xml',
                  'start.html': 'index.html',
                  'pages.html': PAGES_SAVE_AS} 

