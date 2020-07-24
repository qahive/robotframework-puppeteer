import asyncio
from robot.api.deco import not_keyword
from robot.api import logger
from pyppeteer.browser import Browser
from robot.libraries.BuiltIn import BuiltIn
from PuppeteerLibrary.custom_elements.SPage import SPage
from PuppeteerLibrary.base.robotlibcore import DynamicCore
from PuppeteerLibrary.keywords import (
    AlertKeywords,
    AlertKeywordsAsync,
    BrowserManagementKeywords,
    ElementKeywords,
    ElementKeywordsAsync,
    FormElementKeywords,
    FormElementKeywordsAsync,
    JavascriptKeywords,
    JavascriptKeywordsAsync,
    ScreenshotKeywords,
    ScreenshotKeywordsAsync,
    UtilityKeywords,
    WaitingKeywords,
    WaitingKeywordsAsync)

__version__ = '0.4.2'


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

    == Timeout ==
    Timeout will use for Wait.. keywords. By default Puppeteer will use default timeout value if you
    didn't specific in keywords argument.
    Default Timeout is ``30 seconds``.

    User can set new default timeout using ``Set Timeout`` keyword


    *Time format*

    All timeouts and waits can be given as numbers considered seconds (e.g. 0.5 or 42) or in Robot Framework's time syntax(e.g. 1.5 seconds or 1 min 30 s).

    For more information about the time syntax see the Robot Framework User Guide.

    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LISTENER_API_VERSION = 3

    loop = asyncio.get_event_loop()
    browser = None
    current_page = None
    is_load_async_keywords = False
    async_libraries = []

    def __init__(self):
        self.run_on_failure_keyword = 'Capture Page Screenshot'

        libraries = [
            AlertKeywords(self),
            BrowserManagementKeywords(self),
            ElementKeywords(self),
            FormElementKeywords(self),
            JavascriptKeywords(self),
            ScreenshotKeywords(self),
            UtilityKeywords(self),
            WaitingKeywords(self)
        ]
        DynamicCore.__init__(self, libraries)

        self.async_libraries = [
            AlertKeywordsAsync(self),
            ElementKeywordsAsync(self),
            FormElementKeywordsAsync(self),
            JavascriptKeywordsAsync(self),
            ScreenshotKeywordsAsync(self),
            WaitingKeywordsAsync(self)
        ]

    @not_keyword
    def load_async_keywords(self):
        if self.is_load_async_keywords is True:
            return
        self.add_library_components(self.async_libraries)
        self.is_load_async_keywords = True

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

    @not_keyword
    def run_keyword(self, name, args, kwargs):
        self._running_keyword = name
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            self.failure_occurred()
            raise
        finally:
            self._running_keyword = None

    def failure_occurred(self):
        try:
            BuiltIn().run_keyword(self.run_on_failure_keyword)
        except Exception as err:
            logger.warn("Keyword '%s' could not be run on failure: %s"
                        % (self.run_on_failure_keyword, err))
