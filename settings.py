from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']



SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1,
    'participation_fee': 5,
    'doc': "",
}


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'Soles'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 0
POINTS_DECIMAL_PLACES = 0
USE_POINTS = False

ROOMS = []


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
#ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
ADMIN_PASSWORD = 'PACMAN'

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = '^wrnxsj^(6ea-7#&cv*tawwpk*hzov-35m!e^o604&4m^6m+3y'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

ROOMS = [
    {
        'name': 'EconoLab',
        'display_name': 'Laboratorio de Economía',
        'participant_label_file': '_rooms/econolab.txt',
    },
]


SESSION_CONFIGS = [
    {
        'name': 'paper_klo_prosocial',
        'display_name': "Tareas de Prosocialidad",
        'num_demo_participants': 4,
        'app_sequence': ["dictator", "trust", "public_goods", "coin_tossing", "prosociality"],
        'app_names': {"dictator": "primera", "trust": "segunda", "public_goods":"tercera", 
                      "coin_tossing": "cuarta", "prosociality": "quinta"},
        'participation_fee': SESSION_CONFIG_DEFAULTS["participation_fee"],
        'use_browser_bots': False,
        'use_strategy_method': True,
        'pay_random_app': True
    },
    {
        'name': 'paper_klo_au',
        'display_name': "Impuestos & Eficacia de gobierno: Group DEBUG",
        'num_demo_participants': 12,
        'app_sequence': ["real_effort2"],
        'use_browser_bots': False
    },
    {
        'name': 'paper_klo_au',
        'display_name': "Impuestos & Eficacia de gobierno: Authority",
        'num_demo_participants': 2,
        'authority': True,
        'app_sequence': ["real_effort2","survey", 'mpl'],
        'use_browser_bots': False
    },
    {
        'name': 'paper_klo_nau',
        'display_name': "Impuestos & Eficacia de gobierno: No Authority",
        'num_demo_participants': 2,
        'authority': False,
        'app_sequence': ["real_effort2","survey", 'mpl'],
        'use_browser_bots': False
    },  
    {
        'name': 'coin_tossing',
        'display_name': "Coin Tossing - Honesty",
        'num_demo_participants': 1,
        'app_sequence': ['coin_tossing'],
        'pay_random_app': False
    },    
    {
        'name': 'mpl',
        'display_name': "HoltLaury",
        'num_demo_participants': 1,
        'app_sequence': ['mpl'],
    },
    {
       'name': 'public_goods',
       'display_name': "Public Goods",
       'num_demo_participants': 12,
       'app_sequence': ['public_goods'],
       'use_strategy_method': False,
    #    'fixed_matching': True,
    #    'matching_file': "matchings_taxgovcorruption.json"
    },
    {
        'name': 'dictator',
        'display_name': "Dictator: 'Strategy' method",
        'num_demo_participants': 12,
        'app_sequence': ['dictator'],
        # 'fixed_matching': True,
        # 'matching_file': "matchings_taxgovcorruption.json"
    },    
    {
        'name': 'trust',
        'display_name': "Trust Game",
        'num_demo_participants': 12,
        'app_sequence': ['trust'],
        'use_strategy_method': False,
        # 'fixed_matching': True,
        # 'matching_file': "matchings_taxgovcorruption.json"
    },
    {
        'name': 'trust_strategy',
        'display_name': "Trust Game: Strategy Method",
        'num_demo_participants': 12,
        'app_sequence': ['trust'],
        'use_strategy_method': True,
        # 'fixed_matching': True,
        # 'matching_file': "matchings_taxgovcorruption.json"
    },
    {
        'name': 'prosocial',
        'display_name': "Encuesta Prosocialidad",
        'num_demo_participants': 1,
        'app_sequence': ["prosociality"],
        'use_browser_bots': False
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
# otree.settings.augment_settings(globals())

