from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class WaitingKeywords(LibraryComponent):

    @keyword
    def wait_for_request_url(self, url, method, timeout=None):
        """Wait for request url"""
        async def wait_for_request_async():
            await self.ctx.get_current_page().waitForRequest(lambda req: req.url == url and req.method == method, timeout)
        self.loop.run_until_complete(wait_for_request_async())

    @keyword
    def wait_for_response_url(self, url, status=200, timeout=None):
        """Wait for response url"""
        async def wait_for_response_async():
            await self.ctx.get_current_page().waitForResponse(lambda res: res.url == url and res.status == status, timeout)
        self.loop.run_until_complete(wait_for_response_async())

    @keyword
    def wait_until_page_contains_element(self, locator, timeout=None):
        """Wait until page contains element within specific timeout"""
        async def wait_until_page_contains_element_async():
            await self.ctx.get_current_page().waitForSelector_with_selenium_locator(locator, timeout)
        self.loop.run_until_complete(wait_until_page_contains_element_async())

