# Django settings for Goalfish project.

'''
This file is part of Goalfish.es.

Goalfish.es is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Goalfish.es is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Goalfish.es.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import django
# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


ACTIVE_SCHOOL_YEAR='2012'

#AUTHENTICATION_BACKENDS=('django.contrib.auth.backends.ModelBackend','Goalfish.backends.GoalFishAuth.MultiModelBackend',)
AUTHENTICATION_BACKENDS=('Goalfish.backends.GoalFishAuth.MultiModelBackend',)

STUDENT_USER_MODEL='Goalfish.fishes.Student'
TEACHER_USER_MODEL='Goalfish.fishes.Teacher'
PARENT_USER_MODEL='Goalfish.fishes.Parent'
MENTOR_USER_MODEL='Goalfish.fishes.Mentor'
SPONSOR_USER_MODEL='Goalfish.fishes.Sponsor'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Jamie Duncan', 'jduncan@lemonaidstand.net'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(SITE_ROOT, 'sqlite.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zk554xk4ot$*dr2hiitkkie6tu(-f-8=q6rdrm4bz82$+ml#n0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'Goalfish.urls'

TEMPLATE_DIRS = (
                 os.path.join(SITE_ROOT,'static/templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'Goalfish.fishes',
    'Goalfish.goals',
    'Goalfish.messaging',
    'Goalfish.notifications',
    'Goalfish.schools',
    'Goalfish.academics',
    'Goalfish.groups',
    'Goalfish.rewards',
    'Goalfish.sponsorship',
    'Goalfish.django_extensions',
)
