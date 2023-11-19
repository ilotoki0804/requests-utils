import time
import os
import sys

from pytest import MonkeyPatch
import pytest

path = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(path) + '/../'))

from requests_utils import api_with_tools, requests  # noqa: E402


def test_cget() -> None:
    start_time = time.perf_counter()
    api_with_tools.cget('https://naver.com/',
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                               '(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                        avoid_sslerror=True)
    assert time.perf_counter() - start_time >= 0.0001 * 2, 'test have to be refined. 0.0001 is not too slow to test cget function.'

    start_time = time.perf_counter()
    api_with_tools.cget('https://naver.com/',
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                               '(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                        avoid_sslerror=True)
    assert time.perf_counter() - start_time < 0.0001

    with pytest.raises(requests.exceptions.HTTPError):
        requests.get("https://httpbin.org/status/404", raise_for_status=True)

    with pytest.raises(requests.exceptions.ConnectionError):
        requests.get("https://some-invalid-name-website-to-test.com", attempts=2, timeout=0.1)


if __name__ == "__main__":
    test_cget()
