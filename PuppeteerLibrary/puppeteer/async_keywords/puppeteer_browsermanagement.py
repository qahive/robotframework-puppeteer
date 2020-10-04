import sys
from pyppeteer import launch
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.iasync_keywords import iBrowserManagementAsync
from PuppeteerLibrary.custom_elements.SPage import SPage


class PuppeteerBrowserManagement(LibraryComponent):

    async def create_page_async(self) -> SPage:
        new_page = await self.ctx.get_current_context().newPage()
        self.ctx.set_current_page(new_page)
        return self.ctx.get_current_page()

    async def open_browser_async(self, url, browser, alias=None, options=None):
        if self.ctx.browser is None:
            default_args = []
            default_options = {
                'slowMo': 0,
                'headless': True,
                'devtools': False,
                'width': 1366,
                'height': 768
            }
            merged_options = default_options

            if options is not None:
                merged_options = {**merged_options, **options}

            if self.ctx.debug_mode is True:
                merged_options = {**merged_options,
                                  **self.ctx.debug_mode_options}

            if 'win' not in sys.platform.lower():
                default_args = ['--no-sandbox', '--disable-setuid-sandbox']

            self.info(('Open browser to ' + url + '\n' + str(merged_options)))
            self.browser = await launch(
                headless=merged_options['headless'],
                slowMo=merged_options['slowMo'],
                devtools=merged_options['devtools'],
                defaultViewport={
                    'width': merged_options['width'],
                    'height': merged_options['height']
                },
                args=default_args)

        browser_context = await self.browser.createIncognitoBrowserContext()
        await self.ctx.add_context_async(alias, browser_context)
        current_page = await self.create_page_async()
        await current_page.goto(url)
        await current_page.screenshot({'path': 'example.png'})

    async def close_browser_async(self, alias=None):
        pass

    async def close_all_browser_async(self):
        pass
