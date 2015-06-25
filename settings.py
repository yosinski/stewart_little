# Django settings for stewart_little project.
import os

# Get settings from settings_local
try:
    from settings_local import *
except ImportError:
    raise Exception('Could not import settings_local. Did you create it from the template?')

try:
    SECRET_KEY
except NameError:
    raise Exception('You need to define SECRET_KEY in settings_local.py')

# Provide defaults if not imported from settings_local
ADMINS                     = locals().get('ADMINS',  tuple())
MANAGERS                   = locals().get('MANAGERS', ADMINS)
DEBUG                      = locals().get('DEBUG', True)
DANGEROUS_ALL_IPS_INTERNAL = locals().get('DANGEROUS_ALL_IPS_INTERNAL', False)
EXTRA_TEMPLATE_DEBUG       = locals().get('EXTRA_TEMPLATE_DEBUG', False)
TEMPLATE_DEBUG             = locals().get('TEMPLATE_DEBUG', DEBUG or EXTRA_TEMPLATE_DEBUG)
SITE_BASE_DIR              = locals().get('SITE_BASE_DIR', os.path.abspath(os.path.dirname(__file__)))
ADMIN_MEDIA_PREFIX         = locals().get('ADMIN_MEDIA_PREFIX', '/media/admin/')

if len(ADMINS) == 0:
    print('WARNING: no ADMINS defined')

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
STATIC_ROOT   = SITE_BASE_DIR + '/static/'
SITE_URL      = 'http://' + SHORT_SITE_URL
STATIC_URL    = 'static/'

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

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request', # necessary for RequestContext?
    'util.context.add_settings',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'main',
)
