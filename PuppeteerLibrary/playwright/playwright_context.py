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
    contexts = {}
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
        self._reset_context()
    
    def is_server_started(self) -> bool:
        if self.browser is not None:
            return True
        return False

    async def create_new_page(self, options: dict=None):
        self.current_page = await self.browser.newPage()
        return self.current_page

    def _reset_context(self):
        playwright = None
        browser = None
        contexts = {}
        current_page = None
        current_iframe = None

    