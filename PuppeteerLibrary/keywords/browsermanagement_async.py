import time
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class BrowserManagementKeywordsAsync(LibraryComponent):

    @keyword
    async def wait_for_new_window_open_async(self, timeout=None):
        timeout = self.timestr_to_secs_for_default_timeout(timeout)
        pages = await self.ctx.get_browser().pages()
        await pages[-1].title()  # workaround for force pages re-cache
        pre_page_len = len(pages)
        timer = 0
        while timer < timeout:
            pages = await self.ctx.get_browser().pages()
            await pages[-1].title()  # workaround for force pages re-cache
            page_len = len(pages)
            if page_len > pre_page_len:
                return
            timer += 1
            time.sleep(1)
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
