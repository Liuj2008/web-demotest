#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element


class SearchPage(WebPage):
    """搜索类"""

    def __init__(self, driver, page_element="baidu"):
        WebPage.__init__(self, driver=driver)
        self.search = Element(page_element)

    def input_search(self, content):
        """输入搜索"""
        self.input_text(self.search['搜索框'], txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(self.search['候选'])]

    def click_search(self):
        """点击搜索"""
        self.is_click(self.search['搜索按钮'])


if __name__ == '__main__':
    pass
