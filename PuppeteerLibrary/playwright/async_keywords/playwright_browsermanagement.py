from PuppeteerLibrary.keywords.ibrowsermanagement_async import iBrowserManagementAsync
from PuppeteerLibrary.custom_elements.SPage import SPage
try:
    from playwright import async_playwright
except ImportError:
    print('import playwright error')


class PlaywrightBrowserManagement(iBrowserManagementAsync):

    def __init__(self, ctx):
        super().__init__(ctx)

    async def open_browser_async(self, url, browser, alias=None, options=None):
        '''
        if self.ctx.playwright_browser is None:
            playwright = await async_playwright().start()
            self.ctx.playwright_browser = await playwright.webkit.launch(headless=False)
        # page = await self.browser.newPage()
        page = await self._create_page_async()
        '''
        page = await self.ctx.get_library_context(browser).create_new_page()
        await page.goto(url)

    async def close_browser_async(self, alias=None):
        pass

    async def close_all_browser_async(self):
        pass

    async def close_puppeteer_async(self):
        pass

    async def _create_page_async(self):
        new_page = await self.ctx.playwright_browser.newPage()
        return new_page
