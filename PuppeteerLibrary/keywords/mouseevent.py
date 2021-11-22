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

        *Limitation* Drag event only support for css / id locator. Not support for xpath locator or chain locator.
        """
        self.info(f"Mouse move to x: '{x}', y: '{y}'.")
        return self.loop.run_until_complete(self.get_async_keyword_group().mouse_move(x, y))

    @keyword
    def drag_and_drop(self, src_locator, desc_locator):
        """Drag item form sort locator to destination locator

        *Limitation* Drag event only support for css / id locator. Not support for xpath locator or chain locator.
        """
        self.info(f"Draf from '{src_locator}' to '{desc_locator}'.")
        return self.loop.run_until_complete(self.get_async_keyword_group().drag_and_drop(src_locator, desc_locator))
