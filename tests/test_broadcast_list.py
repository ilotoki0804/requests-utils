import os
import sys
from pathlib import Path

import pytest

path = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(path) + '/../'))

from resoup.broadcast_list import (  # noqa: E402
    TagBroadcastList,
    NonchainingBroadcastList,
    AbstractBroadcastList,
    NewTagBroadcastList,
)
from resoup import requests, SoupTools  # noqa: E402

# def test_BroadcastList() -> None:  # TODO


def test_TagBroadcastList() -> None:
    tag_broadcast_list = requests.cget("https://www.python.org/community/logos/").soup_select("img")
    _test_broadcast_list(tag_broadcast_list, TagBroadcastList)
    assert len(tag_broadcast_list[1:2].select("li")[0]) != 0  # type: ignore


def test_NonchainingBroadcastList() -> None:
    tag_broadcast_list = NonchainingBroadcastList(
        requests.cget("https://www.python.org/community/logos/").soup_select("img"))
    _test_broadcast_list(tag_broadcast_list, NonchainingBroadcastList)


def _test_broadcast_list(broadcast_list: AbstractBroadcastList, ListType: type[AbstractBroadcastList]) -> None:
    assert isinstance(broadcast_list, ListType)
    assert len(broadcast_list) != 0
    print(broadcast_list['src'], broadcast_list)
    assert len(broadcast_list['src']) == len(broadcast_list)
    assert broadcast_list['src'] != broadcast_list
    assert broadcast_list[0]
    assert broadcast_list.text
    with pytest.raises(ValueError):
        broadcast_list._callable_attr_broadcast()
