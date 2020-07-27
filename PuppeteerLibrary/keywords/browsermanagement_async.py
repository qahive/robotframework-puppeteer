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
