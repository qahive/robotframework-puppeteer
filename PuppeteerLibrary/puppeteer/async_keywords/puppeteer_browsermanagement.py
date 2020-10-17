import sys
from pyppeteer import launch
from PuppeteerLibrary.keywords.ibrowsermanagement_async import iBrowserManagementAsync
from PuppeteerLibrary.custom_elements.SPage import SPage


class PuppeteerBrowserManagement(iBrowserManagementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def maximize_browser_window(self, width=1366, height=768):
        return await self.ctx.get_current_page().setViewport({
            'width': width,
            'height': height
        })

    async def go_to(self, url):
        return await self.library_ctx.get_current_page().goto(url)

    async def go_back(self):
        return await self.library_ctx.get_current_page().go_back()

    async def reload_page(self):
        return await self.library_ctx.get_current_page().reload_page()

    async def get_window_count(self):
        pass

    async def wait_for_new_window_open(self, timeout=None):
        pass

    async def switch_window(self, locator='MAIN'):
        pass
