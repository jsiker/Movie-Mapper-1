__author__ = 'j3dev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movie_mapper_db',
    }
}

INTERNAL_IPS = ("127.0.0.1", "10.0.2.2")