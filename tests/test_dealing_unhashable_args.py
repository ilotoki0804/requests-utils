import logging
from typing import Sequence, Mapping
import time
from pytest import LogCaptureFixture, raises
import os
import sys

from frozendict import frozendict

path = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(path) + '/../'))

import resoup  # noqa: E402
from resoup import requests  # noqa: E402
from resoup.dealing_unhashable_args import freeze_dict_and_list, made_it_hashable  # noqa: E402


def test_freeze_dict_and_list() -> None:
    def hello(a: Mapping, b: Sequence = ()):
        return a, b

    decorated_hello = freeze_dict_and_list()(hello)

    assert hello(a={1: 2, 3: 4}, b=[1, 2, 3]) == ({1: 2, 3: 4}, [1, 2, 3])
    assert decorated_hello(a={1: 2, 3: 4}, b=[1, 2, 3]) == (frozendict({1: 2, 3: 4}), (1, 2, 3))


class NotHashableMappingIterable:
    def __eq__(self, other):
        return self is other


def test_made_it_hashable(caplog: LogCaptureFixture) -> None:
    hashable = (1, 2, 3)
    mapping = {1: 2, 3: 4, 'foo': 'bar'}
    iterable = [1, 2, 3, 4]
    not_above = NotHashableMappingIterable()
    assert made_it_hashable(hashable) is hashable
    assert made_it_hashable(mapping) == frozendict(mapping)
    assert made_it_hashable(iterable) == tuple(iterable)
    assert made_it_hashable(not_above, alert=False, error=False) is not_above
    made_it_hashable(not_above, alert=True, error=False)
    assert "WARNING" in caplog.text
    with raises(TypeError):
        made_it_hashable(not_above, alert=False, error=True)
    with raises(TypeError):
        made_it_hashable(not_above, alert=True, error=True)
