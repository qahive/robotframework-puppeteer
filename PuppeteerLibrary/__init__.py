from typing import List
from PuppeteerLibrary.base.ipuppeteer_library import iPuppeteerLibrary
import asyncio
from robot.api.deco import not_keyword
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from pyppeteer.browser import Browser, BrowserContext
from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext
from PuppeteerLibrary.library_context.library_context_factory import LibraryContextFactory
from PuppeteerLibrary.custom_elements.SPage import SPage
from PuppeteerLibrary.base.robotlibcore import DynamicCore
from PuppeteerLibrary.keywords import (
    AlertKeywords,
    AlertKeywordsAsync,
    BrowserManagementKeywords,
    BrowserManagementKeywordsAsync,
    DropdownKeywords,
    DropdownKeywordsAsync,
    ElementKeywords,
    ElementKeywordsAsync,
    FormElementKeywords,
    FormElementKeywordsAsync,
    JavascriptKeywords,
    JavascriptKeywordsAsync,
    MockResponseKeywords,
    MockResponseKeywordsAsync,
    MouseEventKeywords,
    MouseEventKeywordsAsync,
    PDFKeywords,
    PDFKeywordsAsync,
    ScreenshotKeywords,
    ScreenshotKeywordsAsync,
    UtilityKeywords,
    WaitingKeywords,
    WaitingKeywordsAsync)


# Get the version from the _version.py versioneer file. For a git checkout,
# this is computed based on the number of commits since the last tag.
from ._version import get_versions
__version__ = str(get_versions()['version']).split('+')[0]
del get_versions


class PuppeteerLibrary(DynamicCore, iPuppeteerLibrary):
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

    loop = None
    is_load_async_keywords = False
    async_libraries = []

    browser = None
    puppeteer_browser: iLibraryContext = None
    playwright_browser: iLibraryContext = None

    # contexts = {}
    current_context_name = None
    current_page = None
    current_iframe = None

    debug_mode = False
    debug_mode_options = {
        'slowMo': 200,
        'devtools': False
    }

    # new context
    current_libary_context: iLibraryContext = None
    library_factory: LibraryContextFactory = None
    library_contexts: dict = {}

    def __init__(self):
        try:
            self.loop = asyncio.get_event_loop()
        except:
            print('Warning: Asyncio not supported')

        self.run_on_failure_keyword = 'Capture Page Screenshot'

        libraries = [
            AlertKeywords(self),
            BrowserManagementKeywords(self),
            DropdownKeywords(self),
            ElementKeywords(self),
            FormElementKeywords(self),
            JavascriptKeywords(self),
            MockResponseKeywords(self),
            MouseEventKeywords(self),
            PDFKeywords(self),
            ScreenshotKeywords(self),
            UtilityKeywords(self),
            WaitingKeywords(self)
        ]
        DynamicCore.__init__(self, libraries)

        self.async_libraries = [
            AlertKeywordsAsync(self),
            BrowserManagementKeywordsAsync(self),
            DropdownKeywordsAsync(self),
            ElementKeywordsAsync(self),
            FormElementKeywordsAsync(self),
            JavascriptKeywordsAsync(self),
            MockResponseKeywordsAsync(self),
            MouseEventKeywordsAsync(self),
            PDFKeywordsAsync(self),
            ScreenshotKeywordsAsync(self),
            WaitingKeywordsAsync(self)
        ]

        self.library_factory = LibraryContextFactory()

    @not_keyword
    def get_current_library_context(self) -> iLibraryContext:
        return self.current_libary_context
    
    @not_keyword
    async def set_current_library_context(self, context_name) -> iLibraryContext:
        self.current_libary_context = self.library_contexts[context_name]
        return self.current_libary_context

    @not_keyword
    def get_library_context_by_name(self, alias: str) -> iLibraryContext:
        return self.library_contexts[alias]

    @not_keyword
    def get_all_library_context(self) -> List[iLibraryContext]:
        return list(self.library_contexts.values())

    @not_keyword
    def create_library_context(self, alias: str, browser_type: str) -> iLibraryContext:
        library_context = self.library_factory.create(browser_type)
        self.library_contexts[alias] = library_context
        self.current_libary_context = library_context
        return library_context    

    @not_keyword
    def load_async_keywords(self):
        if self.is_load_async_keywords is True:
            return
        self.add_library_components(self.async_libraries)
        self.is_load_async_keywords = True

    @not_keyword
    def get_browser(self) -> Browser:
        return self.browser

    @not_keyword
    def clear_browser(self):
        self.browser = None
        self.contexts = {}
        self.current_context_name = None
        self.current_page = None
        self.clear_current_iframe()

    @not_keyword
    async def add_context_async(self, alias, browser_context):
        if alias in self.contexts.keys():
           await self.contexts[alias].close()
           del self.contexts[alias]
        self.current_context_name = alias
        self.contexts[self.current_context_name] = browser_context

    @not_keyword
    # Will obsolted
    async def create_context_async(self, alias) -> BrowserContext:
        context = await self.browser.createIncognitoBrowserContext()
        if alias in self.contexts.keys():
           await self.contexts[alias].close()
           del self.contexts[alias]
        self.current_context_name = alias
        self.contexts[self.current_context_name] = context
        return context

    @not_keyword
    def get_current_context(self) -> BrowserContext:
        return self.contexts[self.current_context_name]

    @not_keyword
    async def set_current_context(self, context_name) -> BrowserContext:
        self.current_context_name = context_name
        context = self.get_current_context()
        pages = await context.pages()
        self.current_page = pages[-1]
        self.clear_current_iframe()
        return context

    @not_keyword
    def clear_context(self, context_name):
        del self.contexts[context_name]
        if self.current_context_name == context_name:
            self.current_context_name = None
            self.current_page = None

    @not_keyword
    def clear_current_context(self):
        self.clear_context(self.current_context_name)

    @not_keyword
    async def create_page_async(self) -> SPage:
        self.current_page = await self.get_current_context().newPage()
        return self.get_current_page()

    @not_keyword
    def get_current_page(self) -> SPage:
        page = self.current_page
        page.__class__ = SPage
        page.selected_iframe = self.current_iframe
        return page

    @not_keyword
    def set_current_page(self, page) -> SPage:
        self.current_page = page
        page.__class__ = SPage
        self.clear_current_iframe()
        return self.current_page

    @not_keyword
    def clear_current_page(self):
        self.current_page = None
        self.clear_current_iframe()

    @not_keyword
    def set_current_iframe(self, iframe):
        self.current_iframe = iframe

    @not_keyword
    def clear_current_iframe(self):
        self.current_iframe = None

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
            BuiltIn().run_keyword_and_ignore_error(self.run_on_failure_keyword)
        except Exception as err:
            logger.warn("Keyword '%s' could not be run on failure: %s"
                        % (self.run_on_failure_keyword, err))

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
