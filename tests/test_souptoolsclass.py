from mailbox import NotEmptyError
from bs4 import BeautifulSoup, Tag
import pytest

from requests_utils import requests, SoupTools
from requests_utils.exceptions import EmptyResultError
from requests_utils.broadcast_list import TagBroadcastList


def test_SoupTools() -> None:
    def test_souptools_instance_contains_html(souptools_instance: SoupTools) -> None:
        RESULT_EXIST_CSS_SELECTOR = "strong"
        INVALID_CSS_SELECTOR = "invalid-css-selector"

        # soup(HTML)
        assert isinstance(souptools_instance.soup(), BeautifulSoup)
        with pytest.warns(UserWarning):
            assert isinstance(souptools_instance.soup("html"), BeautifulSoup)
        assert isinstance(souptools_instance.soup("html.parser"), BeautifulSoup)
        with pytest.warns(UserWarning):
            assert isinstance(souptools_instance.soup("html5"), BeautifulSoup)
        assert isinstance(souptools_instance.soup("html5lib"), BeautifulSoup)
        assert isinstance(souptools_instance.soup("lxml"), BeautifulSoup)

        # soup_select
        assert isinstance(souptools_instance.soup_select(RESULT_EXIST_CSS_SELECTOR), TagBroadcastList)
        assert not isinstance(souptools_instance.soup_select(RESULT_EXIST_CSS_SELECTOR, use_broadcast_list=False),
                              TagBroadcastList)
        assert len(souptools_instance.soup_select(INVALID_CSS_SELECTOR)) == 0, "The selector is not good for test."
        with pytest.raises(EmptyResultError):
            souptools_instance.soup_select(INVALID_CSS_SELECTOR, no_empty_result=True)

        # soup_select_one
        assert isinstance(souptools_instance.soup_select_one(RESULT_EXIST_CSS_SELECTOR), Tag)
        assert souptools_instance.soup_select_one(INVALID_CSS_SELECTOR) is None, "The selector is not good for test."
        with pytest.raises(EmptyResultError):
            souptools_instance.soup_select_one(INVALID_CSS_SELECTOR, no_empty_result=True)

    def test_souptools_instance_contains_html_contains_xml(souptools_instance: SoupTools) -> None:
        RESULT_EXIST_CSS_SELECTOR = "PLANT"
        INVALID_CSS_SELECTOR = "invalid-css-selector"

        # soup(XML)
        assert isinstance(souptools_instance.soup("lxml-xml"), BeautifulSoup)
        assert isinstance(souptools_instance.soup("xml"), BeautifulSoup)
        assert isinstance(souptools_instance.xml(), BeautifulSoup)

        # xml_select
        assert isinstance(souptools_instance.xml_select(RESULT_EXIST_CSS_SELECTOR), TagBroadcastList)
        assert not isinstance(souptools_instance.xml_select(RESULT_EXIST_CSS_SELECTOR, use_broadcast_list=False),
                              TagBroadcastList)
        assert len(souptools_instance.xml_select(INVALID_CSS_SELECTOR)) == 0, "The selector is not good for test."
        with pytest.raises(EmptyResultError):
            souptools_instance.xml_select(INVALID_CSS_SELECTOR, no_empty_result=True)

        # xml_select_one
        assert isinstance(souptools_instance.xml_select_one(RESULT_EXIST_CSS_SELECTOR), Tag)
        assert souptools_instance.xml_select_one(INVALID_CSS_SELECTOR) is None, "The selector is not good for test."
        with pytest.raises(EmptyResultError):
            souptools_instance.xml_select_one(INVALID_CSS_SELECTOR, no_empty_result=True)

    # HTML
    res = requests.get("https://www.python.org")
    souptools_from_text = SoupTools(res.text)
    souptools_from_response = SoupTools.from_response(res)

    test_souptools_instance_contains_html(res)
    test_souptools_instance_contains_html(souptools_from_text)
    test_souptools_instance_contains_html(souptools_from_response)

    # CSS
    res = requests.get("https://www.w3schools.com/xml/plant_catalog.xml")
    souptools_from_text = SoupTools(res.text)
    souptools_from_response = SoupTools.from_response(res)

    test_souptools_instance_contains_html_contains_xml(res)
    test_souptools_instance_contains_html_contains_xml(souptools_from_text)
    test_souptools_instance_contains_html_contains_xml(souptools_from_response)

    with pytest.raises(AttributeError):
        souptools_from_response.some_not_exist_attribute

    # FAIL MESSAGE
    tag_broadcast_list = requests.get("https://httpbin.org/status/404")
    with pytest.raises(EmptyResultError):
        tag_broadcast_list.soup_select("invalid-css-selector", no_empty_result=True)
    with pytest.raises(EmptyResultError):
        tag_broadcast_list.soup_select_one("invalid-css-selector", no_empty_result=True)
