from PuppeteerLibrary.keywords.waiting_async import WaitingKeywordsAsync
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
    def wait_for_function(self, page_function):
        """Wait for page trigger function"""
        return self.loop.run_until_complete(self.async_func.wait_for_function_async(page_function))

    @keyword
    def wait_for_navigation(self):
        """Wait for navigation from any redirect"""
        return self.loop.run_until_complete(self.async_func.wait_for_navigation_async())

    @keyword
    def wait_until_page_contains_element(self, locator, timeout=None):
        """Wait until page contains element within specific timeout"""
        return self.loop.run_until_complete(self.async_func.wait_for_selenium_selector(locator, timeout))

    @keyword
    def wait_until_element_is_hidden(self, locator, timeout=None):
        return self.loop.run_until_complete(self.async_func.wait_until_element_is_hidden_async(locator, timeout))

    @keyword
    def wait_until_element_is_visible(self, locator, timeout=None):
        return self.loop.run_until_complete(self.async_func.wait_until_element_is_visible_async(locator, timeout))

    @keyword
    def wait_until_page_contains(self, text, timeout=None):
        """Waits until ``text`` appears on the current page"""
        return self.loop.run_until_complete(self.async_func.wait_until_page_contains_async(text, timeout))

    @keyword
    def wait_until_page_does_not_contains(self, text, timeout=None):
        """Waits until ``text`` appears on the current page"""
        return self.loop.run_until_complete(self.async_func.wait_until_page_does_not_contains_async(text, timeout))

    @keyword
    def wait_until_element_contains(self, selenium_locator, text, timeout=None):
        """Waits until the ``element`` contains ``text``."""
        return self.loop.run_until_complete(self.async_func.wait_until_element_contains_async(selenium_locator, text, timeout))

    @keyword
    def wait_until_element_does_not_contains(self, selenium_locator, text, timeout=None):
        """Waits until the ``element`` does not contains ``text``."""
        return self.loop.run_until_complete(self.async_func.wait_until_element_does_not_contains_async(selenium_locator, text, timeout))

