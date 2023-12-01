import pytest
from resoup.header_utils import clean_headers


def test_clean_headers() -> None:
    raw_headers = """
Sec-Ch-Ua-Mobile:
?0
Sec-Fetch-Dest:
document
Sec-Fetch-Mode:
navigate
Sec-Fetch-Site:
none
Sec-Fetch-User:
?1
Sec-Gpc:
1
Upgrade-Insecure-Requests:
1
"""
    cleaned_headers = {
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-Gpc': '1',
        'Upgrade-Insecure-Requests': '1'
    }
    assert clean_headers(raw_headers) == cleaned_headers
    with pytest.raises(ValueError):
        clean_headers(raw_headers.replace(":", "", 1))
