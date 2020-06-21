from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class WaitingKeywords(LibraryComponent):

    @keyword
    def wait_until_page_contains_element(self, locator, timeout=None):
        """Wait until page contains element within specific timeout"""
        async def wait_until_page_contains_element_async():
            await self.ctx.get_current_page().waitForSelector_with_selenium_locator(locator, timeout)
        self.loop.run_until_complete(wait_until_page_contains_element_async())
