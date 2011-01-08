from egwexample.settings.common import *


DEBUG = TEMPLATE_DEBUG = True

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'dev.db'

INSTALLED_APPS += (
    'egwdev',
)
