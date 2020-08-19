from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.keywords.mouseevent_async import MouseEventKeywordsAsync


class MouseEventKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = MouseEventKeywordsAsync(self.ctx)

    @keyword
    def mouse_over(self, locator):
        """Simulates hovering the mouse over the element.
        """
        return self.loop.run_until_complete(self.async_func.mouse_over_async(locator))

    @keyword
    def mouse_down(self, locator):
        return self.loop.run_until_complete(self.async_func.mouse_down_async(locator))

    @keyword
    def mouse_up(self):
        return self.loop.run_until_complete(self.async_func.mouse_up_async())

    