import asyncio
from pyppeteer.browser import Browser
from PuppeteerLibrary.custom_elements.SPage import SPage
from robot.api.deco import not_keyword
from PuppeteerLibrary.base.robotlibcore import DynamicCore
from PuppeteerLibrary.keywords import (
    BrowserManagementKeywords,
    ElementKeywords,
    FormElementKeywords)

__version__ = '0.2.0'


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

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__
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
    def get_current_page(self) -> SPage:
        page = self.current_page
        page.__class__ = SPage
        return page

    @not_keyword
    def set_current_page(self, page) -> SPage:
        self.current_page = page
        page.__class__ = SPage
        return self.current_page

    @not_keyword
    def get_browser(self) -> Browser:
        return self.browser
