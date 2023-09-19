if __name__ in {"__main__", "__init__"}:
    import requests_ as requests
    from custom_defaults import CustomDefaults
else:
    from . import requests_ as requests
    from .custom_defaults import CustomDefaults

__title__ = "requests_utils"
__description__ = 'Various convenient features about requests.'
__url__ = "https://github.com/ilotoki0804/requests-utils"
__raw_source_url__ = "https://raw.githubusercontent.com/ilotoki0804/requests-utils/master"
__version_info__ = (0, 2, 3)
__version__ = str.join('.', map(str, __version_info__))
__author__ = "ilotoki0804"
__author_email__ = "ilotoki0804@gmail.com"
__license__ = "MIT License"
