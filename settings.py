# Django settings for stewart_little project.

import os

# Get settings from settings_local
try:
    from settings_local import *
except ImportError:
    raise Exception('Could not import settings_local. Did you create it from the template?')

# Provide defaults if not imported from settings_local
ADMINS                     = locals().get('ADMINS',  (('Jason Yosinski', 'jason.yosinski@gmail.com'),))
MANAGERS                   = locals().get('MANAGERS', ADMINS)
DEBUG                      = locals().get('DEBUG', False)
DANGEROUS_ALL_IPS_INTERNAL = locals().get('DANGEROUS_ALL_IPS_INTERNAL', False)
EXTRA_TEMPLATE_DEBUG       = locals().get('EXTRA_TEMPLATE_DEBUG', False)
TEMPLATE_DEBUG             = locals().get('TEMPLATE_DEBUG', DEBUG or EXTRA_TEMPLATE_DEBUG)
SITE_BASE_DIR              = locals().get('SITE_BASE_DIR', os.path.abspath(os.path.dirname(__file__)))
ADMIN_MEDIA_PREFIX         = locals().get('ADMIN_MEDIA_PREFIX', '/media/admin/')
SERVE_STATIC               = locals().get('SERVE_STATIC', False) # whether to enable static serve

DEFAULT_SQLITE_DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': os.path.join(SITE_BASE_DIR, 'sqlite.db'),             # Or path to database file if using sqlite3.
    'USER': '',                      # Not used with sqlite3.
    'PASSWORD': '',                  # Not used with sqlite3. TODO try removing!
    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
DATABASES                  = locals().get('DATABASES', DEFAULT_SQLITE_DATABASES)

# Derived settings
STATIC_ROOT          = SITE_BASE_DIR + '/static/'
SITE_URL            = 'http://' + SHORT_SITE_URL
MEDIA_URL           = 'http://' + SHORT_SITE_URL + '/static/'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

if DANGEROUS_ALL_IPS_INTERNAL:
    # Make DEBUG available on all IPs
    from fnmatch import fnmatch
    class glob_list(list):
        def __contains__(self, key):
            for elt in self:
                if fnmatch(key, elt): return True
            return False

    INTERNAL_IPS = glob_list([
        '127.0.0.1',
        '*.*.*.*', # Use Debug carefully with this!
        ])

TEMPLATE_DIRS = (
    SITE_BASE_DIR + '/templates',
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lj3f89j(*#FJ(S*JEf98jsflkjF(83jfj;lksjf498hw4gjif3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'accounts.middleware.SavedAnonymousUserMiddleware',   # must be after AuthenticationMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',
    #'util.middleware.ReqRespLogger',
    #'util.middleware.PrintSQL',
)

ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request', # necessary for RequestContext?

    'util.context.add_settings',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backend.SavedAnonymousUserBackend',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.markup',
    'main',
    'util', # for extraFilters
)
