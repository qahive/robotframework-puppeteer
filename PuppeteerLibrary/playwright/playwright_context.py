from PuppeteerLibrary.playwright.async_keywords.playwright_browsermanagement import PlaywrightBrowserManagement
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
    current_page = None
    current_iframe = None
    

    def __init__(self, browser_type: str):
        super().__init__(browser_type)

    async def start_server(self, options: dict=None):
        self.playwright = await async_playwright().start()
        if self.browser_type == "webkit":
            self.browser = await self.playwright.webkit.launch(headless=False)
        elif self.browser_type == "firefox":
            self.browser = await self.playwright.firefox.launch(headless=False)

    async def stop_server(self):
        await self.playwright.stop()
        self._reset_server_context()
    
    def is_server_started(self) -> bool:
        if self.browser is not None:
            return True
        return False

    async def create_new_page(self, options: dict=None):
        self.current_page = await self.browser.newPage()
        return self.current_page

    def get_current_page(self):
        return self.current_page

    async def close_browser_context(self):
        await self.browser.close()
        self._reset_context()

    def get_async_keyword_group(self, keyword_group_name: str):
        switcher = {
            "BrowserManagementKeywords": PlaywrightBrowserManagement(self)
        }
        return switcher.get(keyword_group_name)

    def _reset_context(self):
        self.browser = None
        self.current_page = None
        self.current_iframe = None
    
    def _reset_server_context(self):
        self._reset_context()
        self.playwright = None

    