from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class ElementKeywords(LibraryComponent):

    @keyword
    def click_element(self, locator):
        async def click_element_async():
            print('click element')
            await self.ctx.getCurrentPage().click(locator)
        self.loop.run_until_complete(click_element_async())
