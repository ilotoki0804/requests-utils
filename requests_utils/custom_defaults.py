import functools

if __name__ in {'__main__', 'my_defaults'}:
    import requests_api_with_more_tools
else:
    from . import requests_api_with_more_tools


class CustomDefaults:
    def __init__(
        self,
        **kwargs
    ) -> None:
        self.defaults = kwargs

    def __getattr__(self, name):
        return functools.partial(getattr(requests_api_with_more_tools, name), **self.defaults)
