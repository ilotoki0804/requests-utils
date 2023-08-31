import logging
from typing import Sequence, Mapping
import time

from frozendict import frozendict
import requests_utils
logging.warning('파일이 아닌 설치된 모듈을 실행하고 있습니다.')
from requests_utils import requests

def test_freeze_dict_and_list() -> None:
    freeze_dict_and_list = requests_utils.dealing_unhashable_args.freeze_dict_and_list

    # @freeze_dict_and_list()
    def hello(a: Mapping, b: Sequence = ()):
        # print(a, b)
        return a, b

    hello_decorated = freeze_dict_and_list()(hello)

    assert hello(a={1: 2, 3: 4}, b=[1, 2, 3]) == ({1: 2, 3: 4}, [1, 2, 3])
    assert hello_decorated(a={1: 2, 3: 4}, b=[1, 2, 3]) == (frozendict({1: 2, 3: 4}), (1, 2, 3))

    print('test_freeze_dict_and_list test passed.')


def test_cget() -> None:
    start_time = time.perf_counter()
    requests.cget('http://www.naver.com',
                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                         '(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})
    # print(time.perf_counter() - start_time)
    assert time.perf_counter() - start_time >= 0.0001, 'test have to be refined. 0.0001 is not too slow.'

    start_time = time.perf_counter()
    requests.cget('http://www.naver.com',
                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                         '(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})
    # print(time.perf_counter() - start_time)
    assert time.perf_counter() - start_time < 0.0001

    print('test_cget test passed.')


if __name__ == "__main__":
    test_freeze_dict_and_list()
    test_cget()
