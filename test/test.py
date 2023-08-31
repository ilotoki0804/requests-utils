import logging
from typing import Sequence, Mapping

import requests_utils
logging.warning('파일이 아닌 설치된 모듈을 실행하고 있습니다.')

def test_freeze_dict_and_list():
    freeze_dict_and_list = requests_utils.ignore_unhashable.freeze_dict_and_list

    # @freeze_dict_and_list()
    def hello(a: Mapping, b: Sequence = ()):
        # print(a, b)
        return a, b

    hello_decorated = freeze_dict_and_list()(hello)

    assert hello(a={1: 2, 3: 4}, b=[1, 2, 3]) == ({1: 2, 3: 4}, [1, 2, 3])
    assert hello_decorated(a={1: 2, 3: 4}, b=[1, 2, 3]) == ((1, 3), (1, 2, 3))

    print('test_freeze_dict_and_list test passed.')

if __name__ == "__main__":
    test_freeze_dict_and_list()