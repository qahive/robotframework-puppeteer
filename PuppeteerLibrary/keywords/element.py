from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class ElementKeywords(LibraryComponent):

    @keyword
    def click_element(self, locator):
        self.loop.run_until_complete(self.click_element_async(locator))
        print('click element')

    async def click_element_async(self, locator):
        await self.ctx.getCurrentPage().click(locator)
