from typing import Any
from pyparsing import Optional
from pyppeteer.element_handle import ElementHandle
from pyppeteer.page import Page
from PuppeteerLibrary.locators.CssLocatorParser import CssLocatorParser
from PuppeteerLibrary.locators.IdLocatorParser import IdLocatorParser
from PuppeteerLibrary.locators.XPathLocatorParser import XPathLocatorParser


class SPage(Page):

    def __init__(self):
        super(Page, self).__init__()

    def click(self, selector: str, options: dict = None, **kwargs: Any):
        return super().click(self._getSelector(selector), options)

    '''
    def querySelector(self, selenium_selector: str) -> Optional[ElementHandle]:
        return super().querySelector(self._getSelector(selenium_selector))
    '''

    def _getSelector(self, selenium_selector: str) -> str:
        selector_pair = selenium_selector.split('=', 1)
        if len(selector_pair) != 2:
            selector_pair = selenium_selector.split(':', 1)
        selector_type = selector_pair[0]
        selector_value = selector_pair[1]
        if selector_type == 'id':
            parser = IdLocatorParser()
        elif selector_type == 'xpath':
            parser = XPathLocatorParser()
        elif selector_type == 'css':
            parser = CssLocatorParser()
        else:
            raise Exception('selenium_selector = ' + selenium_selector)
        return parser.parse(selector_value)


"""
How to convert A to B

class A(object):
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super(B, self).__init__()
        self._init_B()
    def _init_B(self):
        self.x += 1

a = A()
b = a
b.__class__ = B
b._init_B()

assert b.x == 2

"""