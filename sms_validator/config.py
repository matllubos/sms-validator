from django.conf import settings as django_settings


DEFAULTS = {
    'MAX_TOKEN_AGE_SECONDS': 60 * 60,
    'TOKEN_LENGTH': 6,
    'UNIVERSAL_TOKEN': None,
}


class Settings(object):

    def __getattr__(self, attr):
        if attr not in DEFAULTS:
            raise AttributeError('Invalid SMS validator setting: "{}"'.format(attr))

        return getattr(django_settings, 'SMS_VALIDATOR_{}'.format(attr), DEFAULTS[attr])


settings = Settings()
