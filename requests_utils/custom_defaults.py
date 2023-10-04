import functools

if __name__ in {'__main__', 'my_defaults'}:
    import requests_utils.api_with_tools as api_with_tools
else:
    from . import api_with_tools


class CustomDefaults:
    def __init__(
        self,
        **kwargs
    ) -> None:
        self.defaults = kwargs

    def __getattr__(self, name):
        return functools.partial(getattr(api_with_tools, name), **self.defaults)
