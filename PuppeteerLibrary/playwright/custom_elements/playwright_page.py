from typing import Any, Dict
from PuppeteerLibrary.custom_elements.base_page import BasePage
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction

try:
    from playwright.page import Page
except Exception:
    from pyppeteer.page import Page
    print('import playwright error')

class PlaywrightPage(BasePage):

    def __init__(self, page: Page):
        self.page = page
        self.selected_iframe = None
    
    def get_page(self) -> Page:
        return self.page

    async def click_with_selenium_locator(self, selenium_locator: str, options: dict = None, **kwargs: Any):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self.page.click_xpath(selector_value, options, **kwargs)
        else:
            await self.page.click(selector_value, options, **kwargs)

    async def click_xpath(self, selector: str, options: dict = None, **kwargs: Any):
        pass

    async def click(self, selector: str, options: dict = None, **kwargs: Any):
        if self.selected_iframe is None:
            return await self.page.click(selector=selector, options=options, kwargs=kwargs)
        else:
            return await self.selected_iframe.click(selector=selector, options=options, kwargs=kwargs)
