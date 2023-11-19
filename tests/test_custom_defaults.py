import time
import os
import sys

from pytest import MonkeyPatch

path = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(path) + '/../'))

from requests_utils.custom_defaults import CustomDefaults  # noqa: E402


def test_CustomDefaults():
    HEADERS = {'User-Agent': 'User Agent for Test'}
    requests = CustomDefaults(headers=HEADERS)
    res = requests.get("https://www.httpbin.org/headers").json()
    assert res['headers']["User-Agent"] == HEADERS["User-Agent"]

    MANUALLY_DEFINED_HEADERS = {'User-Agent': 'Manually Defined User Agent'}
    res = requests.get("https://www.httpbin.org/headers", headers=MANUALLY_DEFINED_HEADERS).json()
    assert res['headers']["User-Agent"] == MANUALLY_DEFINED_HEADERS["User-Agent"]
