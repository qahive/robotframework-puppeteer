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

    def get_selected_frame_or_page(self):
        if self.selected_iframe is not None:
            return self.selected_iframe
        else:
            return self.page

    async def goto(self, url: str):
        self.unselect_iframe()
        return await self.page.goto(url)

    async def go_back(self):
        self.unselect_iframe()
        return await self.page.goBack()

    async def reload_page(self):
        self.unselect_iframe()
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
    async def click_with_selenium_locator(self, selenium_locator: str, options: dict = None, **kwargs: Any):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self._click_xpath(selector_value, options, **kwargs)
        else:
            await self._click(selector_value, options, **kwargs)

    async def _click(self, selector: str, options: dict = None, **kwargs: Any):
        if self.selected_iframe is not None:
            return await self.selected_iframe.click(selector=selector, options=options, kwargs=kwargs)
        else:
            return await self.page.click(selector=selector, options=options, kwargs=kwargs)

    async def _click_xpath(self, selector: str, options: dict = None, **kwargs: Any):
        if self.selected_iframe is not None:
            elements = await self.selected_iframe.xpath(selector)
            return await elements[0].click(options, **kwargs)
        else:
            elements = await self.page.xpath(selector)
            return await elements[0].click(options, **kwargs)

    ############
    # Type
    ############
    async def type_with_selenium_locator(self, selenium_locator: str, text: str, options: dict = None, **kwargs: Any):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self._type_xpath(selector=selector_value, text=text, options=options, kwargs=kwargs)
        else:
            await self._type(selector=selector_value, text=text, options=options, kwargs=kwargs)

    async def _type(self, selector, text: str, options: dict = None, **kwargs: Any):
        if self.selected_iframe is not None:
            return await self.selected_iframe.type(selector=selector, text=text, options=options, kwargs=kwargs)
        else:
            return await self.page.type(selector=selector, text=text, options=options, kwargs=kwargs)

    async def _type_xpath(self, selector, text: str, options: dict = None, **kwargs: Any):
        if self.selected_iframe is not None:
            elements = await self.selected_iframe.xpath(selector)
            await elements[0].type(text, options, **kwargs)
        else:
            elements = await self.page.xpath(selector)
            await elements[0].type(text, options, **kwargs)

    ############
    # Wait
    ############
    async def waitForSelector_with_selenium_locator(self, selenium_locator: str, timeout: float, visible=False, hidden=False):
        options = {
            'timeout': timeout * 1000,
            'visible': visible,
            'hidden': hidden
        }
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            return await self._waitForXPath(xpath=selector_value, options=options)
        else:
            return await self._waitForSelector(selector=selector_value, options=options)

    async def _waitForSelector(self, selector: str, options: dict = None):
        if self.selected_iframe is None:
            return await self.page.waitForSelector(selector=selector, options=options)
        else:
            return await self.selected_iframe.waitForSelector(selector=selector, options=options)

    async def _waitForXPath(self, xpath: str, options: dict = None):
        if self.selected_iframe is None:
            return await self.page.waitForXPath(xpath=xpath, options=options)
        else:
            return await self.selected_iframe.waitForXPath(xpath=xpath, options=options)

    ############
    # Query
    ############
    async def querySelectorAll_with_selenium_locator(self, selenium_locator: str):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            return await self._querySelectorAllForXpath(selector_value)
        else:
            return await self._querySelectorAll(selector_value)
    
    async def querySelector_with_selenium_locator(self, selenium_locator: str):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            return await self._querySelectorForXpath(selector_value)
        else:
            return await self._querySelector(selector_value)

    async def _querySelector(self, selector: str):
        if self.selected_iframe is not None:
            return await self.selected_iframe.querySelector(selector=selector)
        else:
            return await self.page.querySelector(selector=selector)

    async def _querySelectorForXpath(self, selector: str):
        if self.selected_iframe is not None:
            return (await self.selected_iframe.xpath(selector))[0]
        else:
            return (await self.page.xpath(selector))[0]

    async def _querySelectorAll(self, selector: str):
        if self.selected_iframe is not None:
            return await self.selected_iframe.querySelectorAll(selector=selector)
        else:
            return await self.page.querySelectorAll(selector=selector)

    async def _querySelectorAllForXpath(self, selector: str):
        if self.selected_iframe is not None:
            return (await self.selected_iframe.xpath(selector))
        else:
            return (await self.page.xpath(selector))

    ############
    # Select
    ############
    async def select_with_selenium_locator(self, selenium_locator: str, values: str):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self.get_selected_frame_or_page().evaluate('''
                element = document.evaluate('{selector_value}//option[contains(@value, "{values}")]', document, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, values=values))
        else:
            return await self.get_selected_frame_or_page().select(selector_value, values)

    ############
    # Evaluate
    ############
    async def evaluate_with_selenium_locator(self, evaluate: str):
        return await self.get_selected_frame_or_page().evaluate(evaluate)

    ##############################
    # iframe
    ##############################
    def set_current_iframe(self, iframe):
        self.selected_iframe = iframe

    def unselect_iframe(self):
        self.selected_iframe = None
