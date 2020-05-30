from typing import Any
from pyppeteer.page import Page
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction


class SPage(Page):

    def __init__(self):
        super(Page, self).__init__()

    def click(self, selector: str, options: dict = None, **kwargs: Any):
        return super().click(SelectorAbstraction.get_selector(selector), options)

    '''
    def querySelector(self, selenium_selector: str) -> Optional[ElementHandle]:
        return super().querySelector(self._getSelector(selenium_selector))
    '''