import asyncio
import time
import re
from robot.utils import timestr_to_secs
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword


class WaitingKeywordsAsync(LibraryComponent):

    @keyword
    async def wait_for_request_url_async(self, url, method='GET', body=None, timeout=None):
        req = await self.ctx.get_current_page().waitForRequest(
            lambda req: re.search(url, req.url) is not None
                        and req.method == method
            , options={
                'timeout': self.timestr_to_secs_for_default_timeout(timeout) * 1000
            })
        try:
            pos_data = (await req.postData())
        except:
            pos_data = ''
        if body is None or re.search(body, pos_data.replace('\n', '')):
            log_str = 'Wait for request url: '+req.method+' - '+req.url
            if pos_data != '':
                log_str + '\n' + pos_data
            self.info(log_str)
        else:
            raise Exception('Can\'t match request body with ' + body + ' \n ' + pos_data)

    @keyword
    async def wait_for_response_url_async(self, url, status=200, body=None, timeout=None):
        res = await self.ctx.get_current_page().waitForResponse(
            lambda res: re.search(url, res.url) is not None
                        and res.status == int(status)
            , options={
                'timeout': self.timestr_to_secs_for_default_timeout(timeout) * 1000
            })
        try:
            res_text = (await res.text())
        except:
            res_text = ''
        if body is None or re.search(body, res_text.replace('\n','')):
            log_str = 'Wait for request url: ' + res.url
            if res_text != '':
                log_str += '\n' + res_text
            self.info(log_str)
        else:
            raise Exception('Can\'t match response body with '+body+' \n '+res_text)

    @keyword
    async def wait_for_navigation_async(self, timeout=None):
        await self.ctx.get_current_page().waitForNavigation(options={
                'timeout': self.timestr_to_secs_for_default_timeout(timeout) * 1000
            })

    @keyword
    async def wait_for_selenium_selector(self, selenium_locator, timeout=None, visible=False, hidden=False):
        timeout = self.timestr_to_secs_for_default_timeout(timeout)
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
        return await self._wait_until_worker(
            validate_element_contains_text,
            self.timestr_to_secs_for_default_timeout(timeout))

    @keyword
    async def wait_until_element_does_not_contains_async(self, selenium_locator, text, timeout=None):
        async def validate_element_contains_text():
            return (text not in (await (await ( await self.ctx.get_current_page().querySelector_with_selenium_locator(selenium_locator)).getProperty('textContent')).jsonValue()))
        return await self._wait_until_worker(
            validate_element_contains_text,
            self.timestr_to_secs_for_default_timeout(timeout))

    @keyword
    async def wait_until_location_contains_async(self, expected, timeout=None):
        async def validate_url_contains_text():
            return expected in self.ctx.get_current_page().url
        return await self._wait_until_worker(
            validate_url_contains_text,
            self.timestr_to_secs_for_default_timeout(timeout))

    @keyword
    async def wait_until_location_does_not_contains_async(self, expected, timeout=None):
        async def validate_url_not_contains_text():
            return expected not in self.ctx.get_current_page().url
        return await self._wait_until_worker(
            validate_url_not_contains_text,
            self.timestr_to_secs_for_default_timeout(timeout))

    async def _wait_until_worker(self, condition, timeout, error=None):
        max_time = time.time() + timeout
        not_found = None
        while time.time() < max_time:
            try:
                if await condition():
                    return
                else:
                    not_found = None
            except Exception as err:
                not_found = err
            await asyncio.sleep(0.2)
        raise AssertionError(not_found or error)

    def escape_xpath_value(self, value):
        if '"' in value and '\'' in value:
            parts_wo_apos = value.split('\'')
            return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
        if '\'' in value:
            return "\"%s\"" % value
        return "'%s'" % value
