from typing import Any
from pyppeteer.page import Page
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction
from robot.utils import timestr_to_secs


class SPage(Page):

    def __init__(self):
        super(Page, self).__init__()

    async def click_with_selenium_locator(self, selenium_locator: str, options: dict = None, **kwargs: Any):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self.click_xpath(selector_value, options, **kwargs)
        else:
            await self.click(selector_value, options, **kwargs)

    async def click_xpath(self, selector: str, options: dict = None, **kwargs: Any):
        element = await self.xpath(selector)
        await element[0].click(options, **kwargs)

    async def type_with_selenium_locator(self, selenium_locator: str, text: str, options: dict = None, **kwargs: Any):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self.type_xpath(selector_value, text, options, **kwargs)
        else:
            await super().type(selector_value, text, options, **kwargs)

    async def type_xpath(self, selector, text: str, options: dict = None, **kwargs: Any):
        element = await self.xpath(selector)
        await element[0].type(text, options, **kwargs)

    async def querySelectorAll_with_selenium_locator(self, selenium_locator: str):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            return await self.xpath(selector_value)
        else:
            return await self.querySelectorAll(selector_value)

    async def querySelector_with_selenium_locator(self, selenium_locator: str):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            return await self.xpath(selector_value)[0]
        else:
            return await self.querySelector(selector_value)

    async def waitForSelector_with_selenium_locator(self, selenium_locator: str, timeout: float, visible=False, hidden=False):
        options = {
            'timeout': timeout * 1000,
            'visible': visible,
            'hidden': hidden
        }
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            return await self.waitForXPath(selector_value, options)
        else:
            return await self.waitForSelector(selector_value, options)
