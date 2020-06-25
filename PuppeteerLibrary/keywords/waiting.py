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
        return self.loop.run_until_complete(self.async_func.wait_for_selenium_selector(locator, timeout, visible=False, hidden=True))

    @keyword
    def wait_until_element_is_visible(self, locator, timeout=None):
        return self.loop.run_until_complete(self.async_func.wait_for_selenium_selector(locator, timeout, visible=True, hidden=False))

    @keyword
    def wait_until_page_contains(self, text, timeout=None):
        """Waits until ``text`` appears on the current page"""
        locator = "xpath://*[contains(., %s)]" % self.escape_xpath_value(text)
        return self.loop.run_until_complete(self.async_func.wait_for_selenium_selector(locator, timeout))

    def escape_xpath_value(self, value):
        if '"' in value and '\'' in value:
            parts_wo_apos = value.split('\'')
            return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
        if '\'' in value:
            return "\"%s\"" % value
        return "'%s'" % value
