import asyncio
import time
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.utils.device_descriptors import DEVICE_DESCRIPTORS


class BrowserManagementKeywordsAsync(LibraryComponent):

    @keyword
    async def get_window_count_async(self):
        pages = await self.ctx.get_browser().pages()
        for page in pages:
            # Workaround: for force pages re-cache
            try:
                await page.title()
            except:
                return -1
        return len(await self.ctx.get_browser().pages())

    @keyword
    async def wait_for_new_window_open_async(self, timeout=None):
        page_len = 0
        # Workaround:
        # We get length without force reset. For ensure that when we count page length.
        # Page length still not update / same as before open new window
        pre_page_len = len(await self.ctx.get_browser().pages())
        timeout = self.timestr_to_secs_for_default_timeout(timeout)
        max_time = time.time() + timeout
        while time.time() < max_time:
            page_len = await self.get_window_count_async()
            if page_len > pre_page_len:
                return
            await asyncio.sleep(0.5)
        raise Exception('No new page has been open. pre: ' + str(pre_page_len) + ' current: ' + str(page_len))

    @keyword
    async def close_browser_async(self, alias=None):
        if alias is None:
            alias = self.ctx.current_context_name
        await self.ctx.contexts[alias].close()
        self.ctx.clear_context(alias)
        if len(self.ctx.contexts.keys()) > 0:
            await self.ctx.set_current_context(list(self.ctx.contexts.keys())[-1])

    @keyword
    async def close_all_browser_async(self):
        for context in self.ctx.contexts.values():
            await context.close()
        self.ctx.contexts = {}
        self.ctx.current_context_name = None
        self.ctx.current_page = None

    @keyword
    async def close_puppeteer_async(self):
        await self.ctx.browser.close()
        self.ctx.clear_browser()

    @keyword
    async def enable_emulate_mode_async(self, emulate_name):
        await self.ctx.get_current_page().emulate(DEVICE_DESCRIPTORS[emulate_name])

    @keyword
    async def select_frame_async(self, selenium_locator):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        iframe = await element.contentFrame()
        self.ctx.set_current_iframe(iframe)
