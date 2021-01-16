from PuppeteerLibrary.ikeywords.imouseevent_async import iMouseEventAsync
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class MouseEventKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iMouseEventAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def mouse_over(self, locator):
        """Mouse over the element.
        """
        self.info(f"Mouse over '{locator}'.")
        return self.loop.run_until_complete(self.get_async_keyword_group().mouse_over(locator))

    @keyword
    def mouse_down(self, locator):
        """Mouse down on the element.
        """
        self.info(f"Mouse down '{locator}'.")
        return self.loop.run_until_complete(self.get_async_keyword_group().mouse_down(locator))

    @keyword
    def mouse_up(self):
        """Mouse up.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().mouse_up())

    @keyword
    def mouse_move(self, x, y):
        """Move mouse to position x, y.
        """
        self.info(f"Mouse move to x: '{x}', y: '{y}'.")
        return self.loop.run_until_complete(self.get_async_keyword_group().mouse_move(x, y))
