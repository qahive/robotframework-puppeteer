from PuppeteerLibrary.keywords.iwaiting_async import iWaitingAsync


class PlaywrightWaiting(iWaitingAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def _wait_for_selenium_selector(self, selenium_locator, timeout=None, visible=False, hidden=False):
        timeout = self.timestr_to_secs_for_default_timeout(timeout)
        return await self.library_ctx.get_current_page().waitForSelector_with_selenium_locator(selenium_locator, timeout, visible, hidden)

    async def wait_for_request_url(self, url, method='GET', body=None, timeout=None):
        pass

    async def wait_for_response_url(self, url, status=200, body=None, timeout=None):
        pass

    async def wait_for_navigation(self):
        pass

    async def wait_until_page_contains_element(self, locator, timeout=None):
        pass

    async def wait_until_element_is_hidden(self, locator, timeout=None):
        pass

    async def wait_until_element_is_visible(self, locator, timeout=None):
        pass

    async def wait_until_page_contains(self, text, timeout=None):
        pass

    async def wait_until_page_does_not_contains(self, text, timeout=None):
        pass

    async def wait_until_element_contains(self, locator, text, timeout=None):
        pass

    async def wait_until_element_does_not_contains(self, locator, text, timeout=None):
        pass

    async def wait_until_location_contains(self, expected, timeout=None):
        pass

    async def wait_until_location_does_not_contains(self, expected, timeout=None):
        pass

    async def wait_until_element_is_enabled(self, selenium_locator, timeout=None):
        pass

    async def wait_until_element_finished_animating(self, selenium_locator, timeout=None):
        pass

