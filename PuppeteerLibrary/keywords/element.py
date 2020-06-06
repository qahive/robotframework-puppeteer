from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class ElementKeywords(LibraryComponent):

    @keyword
    def click_element(self, selenium_locator):
        async def click_element_async():
            await self.ctx.get_current_page().click_with_selenium_locator(selenium_locator)
        self.loop.run_until_complete(click_element_async())
