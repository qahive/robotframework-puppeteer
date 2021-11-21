from PuppeteerLibrary.utils.coverter import str2bool, str2int
from PuppeteerLibrary.ikeywords.imouseevent_async import iMouseEventAsync


class PuppeteerMouseEvent(iMouseEventAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def mouse_over(self, locator):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        await element.hover()

    async def mouse_down(self, locator):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        bounding_box = await element.boundingBox()
        await self.library_ctx.get_current_page().get_page().mouse.move(
            bounding_box['x'] + bounding_box['width'] / 2,
            bounding_box['y'] + bounding_box['height'] / 2)
        await self.library_ctx.get_current_page().get_page().mouse.down()
    
    async def mouse_up(self):
        await self.library_ctx.get_current_page().get_page().mouse.up()

    async def mouse_move(self, x, y):
        x = str2int(x)
        y = str2int(y)
        await self.library_ctx.get_current_page().get_page().mouse.move(x, y)

    async def drag_and_drop(self, src_locator, desc_locator):
        raise Exception('Not supported for ptchrome. Please use pwchrome')
