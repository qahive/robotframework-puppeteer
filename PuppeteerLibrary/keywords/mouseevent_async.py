from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class MouseEventKeywordsAsync(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx

    @keyword
    async def mouse_over_async(self, selenium_locator):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        await element.hover()

    @keyword
    async def mouse_down_async(self, selenium_locator):
        element = await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)
        await element.hover()
        await self.ctx.get_current_page().mouse.down()

    @keyword
    async def mouse_up_async(self):
        await self.ctx.get_current_page().mouse.up()

    @keyword
    async def mouse_move_async(self, x, y):
        await self.ctx.get_current_page().mouse.move(x, y)
