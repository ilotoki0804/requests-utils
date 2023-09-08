if __name__ in {'__main__', 'my_defaults'}:
    import requests_api_with_more_tools
else:
    from . import requests_api_with_more_tools


class CustomDefaults:
    get = staticmethod(requests_api_with_more_tools.get)
    options = staticmethod(requests_api_with_more_tools.options)
    head = staticmethod(requests_api_with_more_tools.head)
    post = staticmethod(requests_api_with_more_tools.post)
    put = staticmethod(requests_api_with_more_tools.put)
    patch = staticmethod(requests_api_with_more_tools.patch)
    delete = staticmethod(requests_api_with_more_tools.delete)
    cget = staticmethod(requests_api_with_more_tools.cget)
    coptions = staticmethod(requests_api_with_more_tools.coptions)
    chead = staticmethod(requests_api_with_more_tools.chead)
    cpost = staticmethod(requests_api_with_more_tools.cpost)
    cput = staticmethod(requests_api_with_more_tools.cput)
    cpatch = staticmethod(requests_api_with_more_tools.cpatch)
    cdelete = staticmethod(requests_api_with_more_tools.cdelete)
    acget = staticmethod(requests_api_with_more_tools.acget)
    acoptions = staticmethod(requests_api_with_more_tools.acoptions)
    achead = staticmethod(requests_api_with_more_tools.achead)
    acpost = staticmethod(requests_api_with_more_tools.acpost)
    acput = staticmethod(requests_api_with_more_tools.acput)
    acpatch = staticmethod(requests_api_with_more_tools.acpatch)
    acdelete = staticmethod(requests_api_with_more_tools.acdelete)
    aget = staticmethod(requests_api_with_more_tools.aget)
    aoptions = staticmethod(requests_api_with_more_tools.aoptions)
    ahead = staticmethod(requests_api_with_more_tools.ahead)
    apost = staticmethod(requests_api_with_more_tools.apost)
    aput = staticmethod(requests_api_with_more_tools.aput)
    apatch = staticmethod(requests_api_with_more_tools.apatch)
    adelete = staticmethod(requests_api_with_more_tools.adelete)

    def __init__(
            self,
            *,
            method=...,
            url=...,
            attempts=...,
            params=...,
            data=...,
            headers=...,
            cookies=...,
            files=...,
            auth=...,
            timeout=...,
            allow_redirects=...,
            proxies=...,
            hooks=...,
            stream=...,
            verify=...,
            cert=...,
            json=...,
    ):
        ...
