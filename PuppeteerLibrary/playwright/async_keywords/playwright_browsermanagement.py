from PuppeteerLibrary.keywords.ibrowsermanagement_async import iBrowserManagementAsync
from PuppeteerLibrary.custom_elements.SPage import SPage
try:
    from playwright import async_playwright
except ImportError:
    print('import playwright error')


class PlaywrightBrowserManagement(iBrowserManagementAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def maximize_browser_window(self, width=1366, height=768):
        return await self.library_ctx.get_current_page().setViewportSize({
                width: width,
                height: height,
            })

    async def go_to(self, url):
        return await self.library_ctx.get_current_page().goto(url)

    async def go_back(self):
        return await self.library_ctx.get_current_page().goBack()

    async def reload_page(self):
        return await self.library_ctx.get_current_page().reload()

    async def get_window_count(self):
        pages = await self.library_ctx.get_all_pages()
        for page in pages:
            # Workaround: for force pages re-cache
            try:
                await page.title()
            except:
                return -1
        return len(await self.library_ctx.get_all_pages())
        '''
        pages = await self.library_ctx.get_browser().pages()
        for page in pages:
            # Workaround: for force pages re-cache
            try:
                await page.title()
            except:
                return -1
        return len(await self.library_ctx.get_browser().pages())
        '''
    