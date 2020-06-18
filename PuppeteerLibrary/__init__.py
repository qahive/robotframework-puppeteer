import asyncio
from pyppeteer.browser import Browser
from robot.api.deco import not_keyword
from PuppeteerLibrary.base.robotlibcore import keyword, DynamicCore
from PuppeteerLibrary.custom_elements.SPage import SPage
from PuppeteerLibrary.keywords import (
    BrowserManagementKeywords,
    ElementKeywords,
    FormElementKeywords)

__version__ = '0.0.1'


class PuppeteerLibrary(DynamicCore):
    """PuppeteerLibrary is a web testing library for Robot Framework.
    PuppeteerLibrary uses the pyppeteer library internally to
    control a web browser.

    This document explains how to use keywords provided by PuppeteerLibrary.

    == Locator syntax ==
    PuppeteerLibrary supports finding elements based on different strategies
    such as the element id, XPath expressions, or CSS selectors same as SeleniumLibrary

    Locator strategy is specified with a prefix using either syntax ``strategy:value`` or ``strategy=value``.

    | = Strategy = |          = Match based on =         |         = Example =            |
    | id           | Element ``id``.                     | ``id:example``                 |
    | xpath        | XPath expression.                   | ``xpath://div[@id="example"]`` |
    | css          | CSS selector.                       | ``css:div#example``            |
    | link	       | Exact text a link has.	             | ``link:Home page``             |
    | partial link | Partial link text   	             | ``partial link:Home``          |

    """

    ROBOT_LISTENER_API_VERSION = 3

    loop = asyncio.get_event_loop()
    browser = None
    current_page = None

    def __init__(self):
        libraries = [
            BrowserManagementKeywords(self),
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
    def close_browser(self):
        self.loop.run_until_complete(self.close_browser_async())
        print('close')

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
