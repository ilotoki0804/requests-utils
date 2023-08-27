if __name__ in {"__main__", "__init__"}:
    import requests_ as requests
else:
    from . import requests_ as requests

__version__ = (0, 1, 0)
__title__ = "requests_utils"
