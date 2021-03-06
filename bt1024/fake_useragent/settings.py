# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import tempfile

__version__ = '0.0.1'

DB = os.path.join(tempfile.gettempdir(), 'fake_useragent_{version}.json'.format(
    version=__version__,
))

BROWSERS_STATS_PAGE = 'http://www.w3schools.com/browsers/browsers_stats.asp'

BROWSER_BASE_PAGE = 'https://udger.com/resources/ua-list/browser-detail?browser={browser}'

BROWSERS_COUNT_LIMIT = 50

REPLACEMENTS = {
    ' ': '',
    '_': '',
}

SHORTCUTS = {
    'ie': 'ie',
    'msie': 'ie',
    'google': 'chrome',
    'googlechrome': 'chrome',
    'ff': 'firefox',
}

OVERRIDES = {
    'IE': 'ie',
}

HTTP_TIMEOUT = 10

HTTP_RETRIES = 5

HTTP_DELAY = 5