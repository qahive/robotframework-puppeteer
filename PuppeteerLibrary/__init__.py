import asyncio
from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.page import Page
from robot.api.deco import not_keyword
from PuppeteerLibrary.base.robotlibcore import keyword
from SeleniumLibrary.base import DynamicCore

from PuppeteerLibrary.custom_elements.SPage import SPage
from PuppeteerLibrary.keywords import (
    ElementKeywords,
    FormElementKeywords)


__version__ = '0.0.1'


class PuppeteerLibrary(DynamicCore):

    ROBOT_LISTENER_API_VERSION = 3

    loop = asyncio.get_event_loop()
    browser = None
    current_page = None

    def __init__(self):
        libraries = [
            ElementKeywords(self),
            FormElementKeywords(self)
        ]
        DynamicCore.__init__(self, libraries)

    @not_keyword
    def get_browser(self) -> Browser:
        return self.browser

    @not_keyword
    def get_current_page(self) -> SPage:
        page = self.current_page
        page.__class__ = SPage
        return page

    @keyword
    def open_browser(self):
        self.loop.run_until_complete(self.open_browser_async())
        print('open')

    @keyword
    def close_browser(self):
        self.loop.run_until_complete(self.close_browser_async())
        print('close')

    @not_keyword
    async def open_browser_async(self):
        self.browser = await launch(headless=False, defaultViewport={
            'width': 1366,
            'height': 768
        })
        self.current_page = await self.browser.newPage()
        await self.current_page.goto('https://www.w3schools.com/html/html_forms.asp')
        await self.current_page.screenshot({'path': 'example.png'})

    @not_keyword
    async def close_browser_async(self):
        await self.browser.close()

    @keyword
    def maximize_browser_window(self):
        """
        Maximize view port not actual browser and set default size to 1366 x 768
        """
        self.loop.run_until_complete(self.maximize_browser_window_async())

    async def maximize_browser_window_async(self):
        await self.get_current_page().setViewport({
            'width': 1366,
            'height': 768
        })