from robot.libraries.BuiltIn import BuiltIn
from PuppeteerLibrary.keywords.imouseevent_async import iMouseEventAsync


class PlaywrightMouseEvent(iMouseEventAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def mouse_over(self, locator):
        raise Exception('Not implemented')

    async def mouse_down(self, locator):
        raise Exception('Not implemented')
    
    async def mouse_up(self):
        raise Exception('Not implemented')

    async def mouse_move(self, x, y):
        raise Exception('Not implemented')
