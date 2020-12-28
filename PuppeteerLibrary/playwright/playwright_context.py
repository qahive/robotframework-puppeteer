import asyncio
from PuppeteerLibrary.custom_elements.base_page import BasePage
from PuppeteerLibrary.playwright.custom_elements.playwright_page import PlaywrightPage
from PuppeteerLibrary.playwright.async_keywords.playwright_checkbox import PlaywrightCheckbox
from PuppeteerLibrary.playwright.async_keywords.playwright_mockresponse import PlaywrightMockResponse
from PuppeteerLibrary.playwright.async_keywords.playwright_formelement import PlaywrightFormElement
from PuppeteerLibrary.playwright.async_keywords.playwright_dropdown import PlaywrightDropdown
from PuppeteerLibrary.playwright.async_keywords.playwright_alert import PlaywrightAlert
from PuppeteerLibrary.playwright.async_keywords.playwright_screenshot import PlaywrightScreenshot
from PuppeteerLibrary.playwright.async_keywords.playwright_waiting import PlaywrightWaiting
from PuppeteerLibrary.playwright.async_keywords.playwright_element import PlaywrightElement
from PuppeteerLibrary.playwright.async_keywords.playwright_dropdown import PlaywrightDropdown
from PuppeteerLibrary.playwright.async_keywords.playwright_mouseevent import PlaywrightMouseEvent
from PuppeteerLibrary.playwright.async_keywords.playwright_browsermanagement import PlaywrightBrowserManagement
from PuppeteerLibrary.playwright.async_keywords.playwright_pdf import PlaywrightPDF
from PuppeteerLibrary.playwright.async_keywords.playwright_javascript import PlaywrightJavascript
from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext
try:
    from playwright import async_playwright
    from playwright.playwright import Playwright as AsyncPlaywright
    from playwright.browser import Browser
except ImportError:
    print('import playwright error')


class PlaywrightContext(iLibraryContext):

    playwright: any = None
    browser: any = None
    current_page: any = None
    current_iframe = None
    
    def __init__(self, browser_type: str):
        super().__init__(browser_type)

    async def start_server(self, options: dict=None):
        self.playwright = await async_playwright().start()
        if self.browser_type == "webkit":
            self.browser = await self.playwright.webkit.launch(headless=False)
        elif self.browser_type == "firefox":
            self.browser = await self.playwright.firefox.launch(headless=False)    
        self.browser.acceptDownloads = True

    async def stop_server(self):
        await self.playwright.stop()
        self._reset_server_context()
    
    def is_server_started(self) -> bool:
        if self.browser is not None:
            return True
        return False

    async def create_new_page(self, options: dict=None) -> BasePage:
        device_options = {
            'acceptDownloads': True
        }
        if 'emulate' in options:
            device_options = self.playwright.devices[options['emulate']]
        new_page = await self.browser.newPage(**device_options)
        self.current_page = PlaywrightPage(new_page)
        return self.current_page
        
    def get_current_page(self) -> BasePage:
        return self.current_page

    def set_current_page(self, page: any) -> BasePage:
        self.current_page = PlaywrightPage(page)
        return self.current_page

    async def get_all_pages(self):
        return self.browser.contexts[0].pages

    def get_browser_context(self):
        return self.browser

    async def close_browser_context(self):
        if self.browser is not None:
            try:
                await asyncio.wait_for(self.browser.close(), timeout=3)
            except asyncio.TimeoutError:
                None
        self._reset_context()

    async def close_window(self):
        await self.get_current_page().get_page().close()
        pages = await self.get_all_pages()
        self.set_current_page(pages[-1])

    def get_async_keyword_group(self, keyword_group_name: str):
        switcher = {
            "AlertKeywords": PlaywrightAlert(self),
            "BrowserManagementKeywords": PlaywrightBrowserManagement(self),
            "CheckboxKeywords": PlaywrightCheckbox(self),
            "DropdownKeywords": PlaywrightDropdown(self),
            "ElementKeywords": PlaywrightElement(self),
            "FormElementKeywords": PlaywrightFormElement(self),
            "JavascriptKeywords": PlaywrightJavascript(self),
            "MockResponseKeywords": PlaywrightMockResponse(self),
            "MouseEventKeywords": PlaywrightMouseEvent(self),
            "PDFKeywords": PlaywrightPDF(self),
            "ScreenshotKeywords": PlaywrightScreenshot(self),
            "WaitingKeywords": PlaywrightWaiting(self)
        }
        return switcher.get(keyword_group_name)

    def _reset_context(self):
        self.browser = None
        self.current_page = None
        self.current_iframe = None
    
    def _reset_server_context(self):
        self._reset_context()
        self.playwright = None
