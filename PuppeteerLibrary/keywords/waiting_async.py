import asyncio
import time
from robot.utils import timestr_to_secs
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
    async def wait_for_selenium_selector(self, selenium_locator, timeout=None, visible=False, hidden=False):
        await self.ctx.get_current_page().waitForSelector_with_selenium_locator(selenium_locator, timeout, visible, hidden)

    @keyword
    async def wait_until_element_is_hidden_async(self, locator, timeout=None):
        return await self.wait_for_selenium_selector(locator, timeout, visible=False, hidden=True)

    @keyword
    async def wait_until_element_is_visible_async(self, locator, timeout=None):
        return await self.wait_for_selenium_selector(locator, timeout, visible=True, hidden=False)

    @keyword
    async def wait_until_page_contains_async(self, text, timeout=None):
        locator = "xpath://*[contains(., %s)]" % self.escape_xpath_value(text)
        return await self.wait_for_selenium_selector(locator, timeout)

    @keyword
    async def wait_until_page_does_not_contains_async(self, text, timeout=None):
        locator = "xpath://*[contains(., %s)]" % self.escape_xpath_value(text)
        return await self.wait_for_selenium_selector(locator, timeout, visible=False, hidden=True)

    @keyword
    async def wait_until_element_contains_async(self, selenium_locator, text, timeout=None):
        async def validate_element_contains_text():
            return (text in (await (await ( await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)).getProperty('textContent')).jsonValue()))
        return await self._wait_until(
            validate_element_contains_text,
            timeout)

    @keyword
    async def wait_until_element_does_not_contains_async(self, selenium_locator, text, timeout=None):
        async def validate_element_contains_text():
            return (text not in (await (await ( await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)).getProperty('textContent')).jsonValue()))
        return await self._wait_until(
            validate_element_contains_text,
            timeout)

    async def _wait_until(self, condition, error, timeout=None):
        if timeout is None:
            timeout = '30s'
        timeout = timestr_to_secs(timeout)
        await self._wait_until_worker(condition, timeout, error)

    async def _wait_until_worker(self, condition, timeout, error):
        max_time = time.time() + timeout
        not_found = None
        while time.time() < max_time:
            try:
                if await condition():
                    return
            except Exception as err:
                not_found = err
            else:
                not_found = None
            await asyncio.sleep(0.2)
        raise AssertionError(not_found or error)

    def escape_xpath_value(self, value):
        if '"' in value and '\'' in value:
            parts_wo_apos = value.split('\'')
            return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
        if '\'' in value:
            return "\"%s\"" % value
        return "'%s'" % value
