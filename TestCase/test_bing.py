#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage


@allure.feature("测试Bing模块")
class TestBingSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_searchpage(self, drivers):
        """打开搜索页面"""
        search = SearchPage(drivers, page_element="bing")
        search.get_url(ini.getPageUrl("bing"))

    @allure.story("搜索selenium结果用例")
    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers, page_element="bing")
        search.input_search("selenium")
        search.click_search()
        result = re.search(r'selenium', search.get_source)
        log.info(result)
        assert result

    @allure.story("测试搜索候选用例")
    def test_002(self, drivers):
        """测试搜索候选"""
        search = SearchPage(drivers, page_element="bing")
        search.input_search("selenium")
        log.info(list(search.imagine))
        assert all(["selenium" in i for i in search.imagine])


# if __name__ == '__main__':
#     pytest.main(['TestCase/test_bing.py'])
