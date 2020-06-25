from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class WaitingKeywordsAsync(LibraryComponent):

    @keyword
    async def wait_for_request_url_async(self, url, method='GET', timeout=None):
        return await self.ctx.get_current_page().waitForRequest(
            lambda req: req.url == url and req.method == method, timeout)

    @keyword
    async def wait_for_response_url_async(self, url, status=200, timeout=None):
        await self.ctx.get_current_page().waitForResponse(lambda res: res.url == url and res.status == status, timeout)

    @keyword
    async def wait_for_function_async(self, page_function):
        await self.ctx.get_current_page().waitForFunction(page_function)

    @keyword
    async def wait_for_navigation_async(self):
        await self.ctx.get_current_page().waitForNavigation()

    @keyword
    async def wait_until_page_contains_element_async(self, locator, timeout=None):
        await self.ctx.get_current_page().waitForSelector_with_selenium_locator(locator, timeout)

    @keyword
    async def wait_until_page_does_not_contains_element_async(self, locator, timeout=None):
        await self.ctx.get_current_page().waitForSelector_with_selenium_locator(locator, timeout, visible=False, hidden=True)
