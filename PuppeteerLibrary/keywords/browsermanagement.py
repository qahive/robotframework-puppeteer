from pyppeteer import launch
from pyppeteer.browser import Browser
from robot.api.deco import not_keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class BrowserManagementKeywords(LibraryComponent):

    @keyword
    def open_browser(self):
        async def open_browser_async():
            self.browser = await launch(headless=False, defaultViewport={
                'width': 1366,
                'height': 768
            })
            self.ctx.current_page = await self.browser.newPage()
            await self.ctx.current_page.goto('https://www.w3schools.com/html/html_forms.asp')
            await self.ctx.current_page.screenshot({'path': 'example.png'})
        self.loop.run_until_complete(open_browser_async())

    @not_keyword
    def get_browser(self) -> Browser:
        return self.browser

    @keyword
    def close_browser(self):
        async def close_browser_async():
            await self.browser.close()
        self.loop.run_until_complete(close_browser_async())

    @keyword
    def maximize_browser_window(self):
        """
        Maximize view port not actual browser and set default size to 1366 x 768
        """
        async def maximize_browser_window_async():
            await self.ctx.get_current_page().setViewport({
                'width': 1366,
                'height': 768
            })
        self.loop.run_until_complete(maximize_browser_window_async())

    @keyword
    def close_all_browsers(self):
        print('')


    @keyword
    def switch_browser(self, index_or_alias):
        print('')

    @keyword
    def get_source(self):
        print('')

    @keyword
    def get_title(self):
        print('')

    @keyword
    def get_location(self):
        print('')

    @keyword
    def go_back(self):
        print('')

    @keyword
    def go_to(self, url):
        print('')

    @keyword
    def reload_page(self):
        print('')
