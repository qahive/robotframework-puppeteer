from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class MouseEventKeywordsAsync(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx

    @keyword
    async def mouse_over_async(self, selenium_locator):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        await element.hover()
