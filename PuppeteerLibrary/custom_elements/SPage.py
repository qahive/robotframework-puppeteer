from typing import Any, Optional, List
from pyppeteer.element_handle import ElementHandle
from pyppeteer.page import Page
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction


class SPage(Page):

    def __init__(self):
        super(Page, self).__init__()

    def click(self, selector: str, options: dict = None, **kwargs: Any):
        return super().click(SelectorAbstraction.get_selector(selector), options, **kwargs)

    def type(self, selector: str, text: str, options: dict = None, **kwargs: Any):
        return super().type(SelectorAbstraction.get_selector(selector), text, options, **kwargs)

    def tap(self, selector: str):
        return super().tap(SelectorAbstraction.get_selector(selector))

    def querySelector(self, selector: str) -> Optional[ElementHandle]:
        return super().querySelector(self._getSelector(selector))

    def querySelectorAll(self, selector: str) -> List[ElementHandle]:
        return super().querySelectorAll(SelectorAbstraction.get_selector(selector))
