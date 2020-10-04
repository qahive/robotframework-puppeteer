from PuppeteerLibrary.base.librarycomponent import LibraryComponent
try:
    from playwright import async_playwright
except ImportError:
    print('import playwright error')


class PlaywrightBrowserManagement(LibraryComponent):

    async def start_server_async(self, browser, options: dict = None):
        playwright = await async_playwright().start()
        self.browser = await playwright.webkit.launch(headless=False)
        return self.browser

    async def open_browser_async(self, url, browser, alias=None, options=None):
        if self.ctx.browser is None:
            self.start_server_async(browser, options)
        page = await self.browser.newPage()
        await page.goto(url)

    async def close_browser_async(self, alias=None):
        pass

    async def close_all_browser_async(self):
        pass
