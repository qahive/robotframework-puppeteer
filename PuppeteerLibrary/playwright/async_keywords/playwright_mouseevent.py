from PuppeteerLibrary.locators import SelectorAbstraction
from PuppeteerLibrary.utils.coverter import str2int, str2str
import time
from robot.libraries.BuiltIn import BuiltIn
from PuppeteerLibrary.ikeywords.imouseevent_async import iMouseEventAsync


class PlaywrightMouseEvent(iMouseEventAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def mouse_over(self, locator):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        await element.hover()

    async def mouse_down(self, locator):
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        bounding_box = await element.bounding_box()
        await self.library_ctx.get_current_page().get_page().mouse.move(
            bounding_box['x'] + bounding_box['width'] / 2,
            bounding_box['y'] + bounding_box['height'] / 2)
        await self.library_ctx.get_current_page().get_page().mouse.down()
        # TODO: Workaround for firefox not throw exception when mouse down and then mouse move
        time.sleep(0.5)
    
    async def mouse_up(self):
        await self.library_ctx.get_current_page().get_page().mouse.up()

    async def mouse_move(self, x, y):
        x = str2int(x)
        y = str2int(y)
        await self.library_ctx.get_current_page().get_page().mouse.move(x, y)

    async def drag_and_drop(self, src_locator, desc_locator):
        src_locator_value = SelectorAbstraction.get_selector(src_locator)
        desc_locator_value = SelectorAbstraction.get_selector(desc_locator)
        await self.library_ctx.get_current_page().get_page().drag_and_drop(src_locator_value, desc_locator_value)
