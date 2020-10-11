from PuppeteerLibrary.keywords.ibrowsermanagement_async import iBrowserManagementAsync
from PuppeteerLibrary.custom_elements.SPage import SPage
try:
    from playwright import async_playwright
except ImportError:
    print('import playwright error')


class PlaywrightBrowserManagement(iBrowserManagementAsync):

    def __init__(self, ctx):
        super().__init__(ctx)

    async def go_to(self, url):
        return await self.ctx.get_current_page().goto(url)
