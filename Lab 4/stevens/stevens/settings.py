# Add '*' to ALLOWED_HOSTS

ALLOWED_HOSTS = ['*']

# Add 'myapp' to INSTALLED_APPS
# The comma after 'myapp' is required

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

# The default database is SQLite3
# If desired, change database to MySQL

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',    
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'stevens',
        'USER': 'pi',
        'PASSWORD': 'miguel',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# If desired, change the default UTC TIME_ZONE

TIME_ZONE = 'America/New_York'