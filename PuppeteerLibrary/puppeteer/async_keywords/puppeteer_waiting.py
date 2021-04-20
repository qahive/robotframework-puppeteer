from PuppeteerLibrary.utils.coverter import str2int, str2str
import asyncio
import re
import time
from robot.utils.dotdict import DotDict
from PuppeteerLibrary.ikeywords.iwaiting_async import iWaitingAsync


class PuppeteerWaiting(iWaitingAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def _wait_for_selenium_selector(self, selenium_locator, timeout=None, visible=False, hidden=False):
        timeout = self.timestr_to_secs_for_default_timeout(timeout)
        return await self.library_ctx.get_current_page().waitForSelector_with_selenium_locator(selenium_locator, timeout, visible, hidden)
    
    def escape_xpath_value(self, value):
        if '"' in value and '\'' in value:
            parts_wo_apos = value.split('\'')
            return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
        if '\'' in value:
            return "\"%s\"" % value
        return "'%s'" % value

    async def wait_for_request_url(self, url, method='GET', body=None, timeout=None):
        url = str2str(url)
        method = str2str(method)
        req = await self.library_ctx.get_current_page().get_page().waitForRequest(
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

        return DotDict({
            'url': req.url,
            'method': req.method,
            'body':  pos_data
        })

    async def wait_for_response_url(self, url, status=200, body=None, timeout=None):
        url = str2str(url)
        status = str2int(status)
        res = await self.library_ctx.get_current_page().get_page().waitForResponse(
            lambda res: re.search(url, res.url) is not None
                        and res.status == status
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
        return DotDict({
            'url': res.url,
            'status': res.status,
            'body': res_text
        })

    async def wait_for_navigation(self, timeout=None):
        await self.library_ctx.get_current_page().get_page().waitForNavigation(
            options={
                'timeout': self.timestr_to_secs_for_default_timeout(timeout) * 1000
            })

    async def wait_until_page_contains_element(self, locator, timeout=None):
        return await self._wait_for_selenium_selector(locator, timeout, visible=True, hidden=False)

    async def wait_until_element_is_hidden(self, locator, timeout=None):
        return await self._wait_for_selenium_selector(locator, timeout, visible=False, hidden=True)

    async def wait_until_element_is_visible(self, locator, timeout=None):
        return await self._wait_for_selenium_selector(locator, timeout, visible=True, hidden=False)

    async def wait_until_page_contains(self, text, timeout=None):
        text = str2str(text)
        locator = "xpath://*[contains(., %s)]" % self.escape_xpath_value(text)
        return await self._wait_for_selenium_selector(locator, timeout, visible=True, hidden=False)

    async def wait_until_page_does_not_contains(self, text, timeout=None):
        text = str2str(text)
        locator = "xpath://*[contains(., %s)]" % self.escape_xpath_value(text)
        return await self._wait_for_selenium_selector(locator, timeout, visible=False, hidden=True)

    async def wait_until_element_contains(self, locator, text, timeout=None):
        text = str2str(text)
        async def validate_element_contains_text():
            return (text in (await (await ( await self.library_ctx.get_current_page().
                querySelector_with_selenium_locator(locator)).getProperty('textContent')).jsonValue()))
        return await self._wait_until_worker(
            validate_element_contains_text,
            self.timestr_to_secs_for_default_timeout(timeout))

    async def wait_until_element_does_not_contains(self, locator, text, timeout=None):
        text = str2str(text)
        async def validate_element_contains_text():
            return (text not in (await (await ( await self.library_ctx.get_current_page().
                querySelector_with_selenium_locator(locator)).getProperty('textContent')).jsonValue()))
        return await self._wait_until_worker(
            validate_element_contains_text,
            self.timestr_to_secs_for_default_timeout(timeout))

    async def wait_until_location_contains(self, expected, timeout=None):
        expected = str2str(expected)
        async def validate_url_contains_text():
            return expected in self.library_ctx.get_current_page().get_page().url
        return await self._wait_until_worker(
            validate_url_contains_text,
            self.timestr_to_secs_for_default_timeout(timeout))

    async def wait_until_location_does_not_contains(self, expected, timeout=None):
        expected = str2str(expected)
        async def validate_url_not_contains_text():
            return expected not in self.library_ctx.get_current_page().get_page().url
        return await self._wait_until_worker(
            validate_url_not_contains_text,
            self.timestr_to_secs_for_default_timeout(timeout))

    async def wait_until_element_is_enabled(self, locator, timeout=None):
        async def validate_is_enabled():
            element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
            is_disabled = await (await element.getProperty('disabled')).jsonValue()
            return is_disabled == False
        return await self._wait_until_worker(
            validate_is_enabled,
            self.timestr_to_secs_for_default_timeout(timeout),
            'Element '+locator+' was not enabled.')

    async def wait_until_element_finished_animating(self, locator, timeout=None):
        prev_rect_tmp = { 'value': None }
        async def check_finished_animating():
            await self.wait_until_element_is_visible(locator)
            element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
            if prev_rect_tmp['value'] is None:
                prev_rect_tmp['value'] = await element.boundingBox()
                return False
            prev_rect = prev_rect_tmp['value']
            next_rect = await element.boundingBox()
            if next_rect['x'] == prev_rect['x'] and next_rect['y'] == prev_rect['y']:
                return True
            else:
                prev_rect_tmp['value'] = next_rect
                return False
        return await self._wait_until_worker(
            check_finished_animating,
            self.timestr_to_secs_for_default_timeout(timeout),
            'Element '+locator+' was not enabled.')

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
