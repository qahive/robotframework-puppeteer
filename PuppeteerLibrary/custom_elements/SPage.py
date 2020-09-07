from typing import Any, List, Optional
from pyppeteer.element_handle import ElementHandle
from pyppeteer.page import Page
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction
from robot.utils import timestr_to_secs


class SPage(Page):
    selected_iframe: ElementHandle = None

    def __init__(self):
        super(Page, self).__init__()
        self.selected_iframe = None

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
            await self.type_xpath(selector=selector_value, text=text, options=options, kwargs=kwargs)
        else:
            await super().type(selector=selector_value, text=text, options=options, kwargs=kwargs)

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
            return (await self.xpath(selector_value))[0]
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
            return await self.waitForXPath(xpath=selector_value, options=options)
        else:
            return await self.waitForSelector(selector=selector_value, options=options)

    # Override waitForXPath behavior for SPage
    async def waitForXPath(self, xpath: str, options: dict = None, **kwargs: Any):
        if self.selected_iframe is None:
            return await super().waitForXPath(xpath=xpath, options=options, kwargs=kwargs)
        else:
            return await self.selected_iframe.waitForXPath(xpath=xpath, options=options, kwargs=kwargs)

    # Override waitForSelector behavior for SPage
    async def waitForSelector(self, selector: str, options: dict = None, **kwargs: Any):
        if self.selected_iframe is None:
            return await super().waitForSelector(selector=selector, options=options, kwargs=kwargs)
        else:
            return await self.selected_iframe.waitForSelector(selector=selector, options=options, kwargs=kwargs)

    # Override xpath behavior for SPage
    async def xpath(self, expression: str) -> List[ElementHandle]:
        if self.selected_iframe is None:
            return await super().xpath(expression=expression)
        else:
            return await self.selected_iframe.xpath(expression=expression)

    # Override click behavior for SPage
    async def click(self, selector: str, options: dict = None, **kwargs: Any):
        if self.selected_iframe is None:
            return await super().click(selector=selector, options=options, kwargs=kwargs)
        else:
            return await self.selected_iframe.click(selector=selector, options=options, kwargs=kwargs)

    # Override querySelectorAll for SPage
    async def querySelector(self, selector: str) -> Optional[ElementHandle]:
        if self.selected_iframe is None:
            return await super().querySelector(selector=selector)
        else:
            return await self.selected_iframe.querySelector(selector=selector)
