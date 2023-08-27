if __name__ in {"__main__", "__init__"}:
    import requests_ as requests
    from custom_defaults import CustomDefaults
else:
    from . import requests_ as requests
    from .custom_defaults import CustomDefaults

__version__ = (0, 1, 0)
__title__ = "requests_utils"
