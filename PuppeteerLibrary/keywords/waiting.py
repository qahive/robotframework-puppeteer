from PuppeteerLibrary.keywords.waiting_async import WaitingKeywordsAsync
from robot.api.deco import not_keyword

from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class WaitingKeywords(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.async_func = WaitingKeywordsAsync(self.ctx)

    @keyword
    def wait_for_request_url(self, url, method='GET', timeout=None):
        """Wait for request url"""
        return self.loop.run_until_complete(self.async_func.wait_for_request_url_async(url, method , timeout))

    @keyword
    def wait_for_response_url(self, url, status=200, timeout=None):
        """Wait for response url"""
        return self.loop.run_until_complete(self.async_func.wait_for_response_url_async(url, status, timeout))

    @keyword
    def wait_until_page_contains_element(self, locator, timeout=None):
        """Wait until page contains element within specific timeout"""
        return self.loop.run_until_complete(self.async_func.wait_until_page_contains_element_async(locator, timeout))
