from typing import Any
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

    async def goto(self, url: str):
        return await self.page.goto(url)

    async def go_back(self):
        return await self.page.goBack()

    async def reload_page(self):
        return await self.page.reload()

    async def title(self):
        return await self.page.title()

    async def set_viewport_size(self, width: int, height: int):
        return await self.page.setViewportSize(width, height)

    ############
    # Click
    ############
    async def click_with_selenium_locator(self, selenium_locator: str, options: dict = None, **kwargs: Any):
        if options is None:
            options = {}
        selector_value = SelectorAbstraction.get_selector(selenium_locator)

        if self.selected_iframe is not None:
            return await self.selected_iframe.click(selector=selenium_locator, **options)
        else:
            return await self.page.click(selector=selenium_locator, **options)

    ############
    # Type
    ############
    async def type_with_selenium_locator(self, selenium_locator: str, text: str, options: dict = None, **kwargs: Any):
        if options is None:
            options = {}
        if self.selected_iframe is not None:
            return await self.selected_iframe.type(selector=selenium_locator, text=text, **options)
        else:
            return await self.page.type(selector=selenium_locator, text=text, **options)

    ############
    # Wait
    ############
    async def waitForSelector_with_selenium_locator(self, selenium_locator: str, timeout: float, visible=False, hidden=False):
        options = {
            'timeout': timeout * 1000,
            'state': 'visible'
        }
        if visible is True:
            options['state'] = 'visible'
        if hidden is True:
            options['state'] = 'hidden'

        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        return await self.get_page().waitForSelector(
            selector=selector_value, 
            timeout=options['timeout'], 
            state=options['state'])

    ############
    # Query
    ############
    async def querySelector(self, selector: str):
        if self.selected_iframe is not None:
            return await self.selected_iframe.querySelector(selector=selector)
        else:
            return await self.get_page().querySelector(selector=selector)

    async def querySelectorAll_with_selenium_locator(self, selenium_locator: str):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            return await self.get_page().xpath(selector_value)
        else:
            return await self.get_page().querySelectorAll(selector_value)
    
    async def querySelector_with_selenium_locator(self, selenium_locator: str):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            return (await self.get_page().xpath(selector_value))[0]
        else:
            return await self.get_page().querySelector(selector_value)

    ##############################
    # iframe
    ##############################
    def set_current_iframe(self, iframe):
        self.selected_iframe = iframe

    def unselect_iframe(self):
        self.selected_iframe = None
