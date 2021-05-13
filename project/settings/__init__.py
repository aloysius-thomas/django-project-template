from decouple import config

environment = config('ENV') or None  # Change According to environment

if environment == 'prod':
    from .prod import *
elif environment == 'dev':
    from .dev import *
elif environment == 'uat':
    from .uat import *
else:
    raise KeyError('please create an environment variable .env file and specific "ENV" ')
