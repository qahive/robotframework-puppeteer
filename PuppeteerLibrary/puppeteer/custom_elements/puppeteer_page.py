from typing import Any
from pyppeteer.page import Page
from PuppeteerLibrary.custom_elements.base_page import BasePage
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction


class PuppeteerPage(BasePage):

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
        self.page.setViewport({
            width: width,
            height: height
        })

    ############
    # Click
    ############
    async def click(self, selector: str, options: dict = None, **kwargs: Any):
        pass
        '''
        if self.selected_iframe is None:
            return await self.page.click(selector=selector, options=options, kwargs=kwargs)
        else:
            return await self.selected_iframe.click(selector=selector, options=options, kwargs=kwargs)
        '''

    async def click_with_selenium_locator(self, selenium_locator: str, options: dict = None, **kwargs: Any):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self.page.click_xpath(selector_value, options, **kwargs)
        else:
            await self.page.click(selector_value, options, **kwargs)

    async def click_xpath(self, selector: str, options: dict = None, **kwargs: Any):
        pass

    ############
    # Type
    ############
    async def type_with_selenium_locator(self, selenium_locator: str, text: str, options: dict = None, **kwargs: Any):
        pass

    async def type_xpath(self, selector, text: str, options: dict = None, **kwargs: Any):
        pass

    ############
    # Wait
    ############
    async def waitForSelector_with_selenium_locator(self, selenium_locator: str, timeout: float, visible=False, hidden=False):
        pass
        '''
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
        '''

    ############
    # Query
    ############
    async def querySelector(self, selector: str):
        pass

    async def querySelectorAll_with_selenium_locator(self, selenium_locator: str):
        pass
    
    async def querySelector_with_selenium_locator(self, selenium_locator: str):
        pass

