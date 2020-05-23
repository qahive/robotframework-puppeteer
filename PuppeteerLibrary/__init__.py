import asyncio
from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.page import Page

from PuppeteerLibrary.base.robotlibcore import keyword
from SeleniumLibrary.base import DynamicCore
from PuppeteerLibrary.keywords import (
    ElementKeywords
)


__version__ = '0.0.1'


class PuppeteerLibrary(DynamicCore):

    ROBOT_LISTENER_API_VERSION = 3

    loop = asyncio.get_event_loop()
    browser = None
    current_page = None

    def __init__(self):
        libraries = [
            ElementKeywords(self)
        ]
        DynamicCore.__init__(self, libraries)

    def _getBrowser(self) -> Browser:
        return self.browser

    def _getCurrentPage(self) -> Page:
        return self.current_page

    @keyword
    def open_browser(self):
        self.loop.run_until_complete(self.open_browser_async())
        print('open')

    @keyword
    def close_browser(self):
        self.loop.run_until_complete(self.close_browser_async())
        print('close')

    async def open_browser_async(self):
        self.browser = await launch(headless=False)
        self.current_page = await self.browser.newPage()
        await self.current_page.goto('http://example.com')
        await self.current_page.screenshot({'path': 'example.png'})

    async def close_browser_async(self):
        await self.browser.close()
