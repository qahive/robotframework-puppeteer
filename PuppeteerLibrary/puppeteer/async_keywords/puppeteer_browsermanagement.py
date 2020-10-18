import asyncio
import re
import time
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
        page_len = 0
        # Workaround:
        # We get length without force reset. For ensure that when we count page length.
        # Page length still not update / same as before open new window
        pre_page_len = len(await self.library_ctx.get_all_pages())
        timeout = self.timestr_to_secs_for_default_timeout(timeout)
        max_time = time.time() + timeout
        while time.time() < max_time:
            page_len = await self._get_window_count_async()
            if page_len > pre_page_len:
                return
            await asyncio.sleep(0.5)
        raise Exception('No new page has been open. pre: ' + str(pre_page_len) + ' current: ' + str(page_len))

    async def _get_window_count_async(self):
        pages = await self.library_ctx.get_all_pages()
        for page in pages:
            # Workaround: for force pages re-cache
            try:
                await page.title()
            except:
                return []
        return len(await self.library_ctx.get_all_pages())

    async def switch_window(self, locator='MAIN'):
        pass
