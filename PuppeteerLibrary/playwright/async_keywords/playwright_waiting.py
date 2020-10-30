import asyncio
import re
import time
from robot.utils.dotdict import DotDict
from PuppeteerLibrary.ikeywords.iwaiting_async import iWaitingAsync


class PlaywrightWaiting(iWaitingAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def wait_for_request_url(self, url, method='GET', body=None, timeout=None):
        req = await self.library_ctx.get_current_page().get_page().waitForEvent(
            "request", lambda request: re.search(url, request.url) is not None and request.method == method,
            self.timestr_to_secs_for_default_timeout(timeout) * 1000 
        )
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
        res = await self.library_ctx.get_current_page().get_page().waitForEvent(
            "response", lambda response: re.search(url, response.url) is not None and response.status == int(status),
            self.timestr_to_secs_for_default_timeout(timeout) * 1000 
        )
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
        raise Exception('Not implemented.')

    async def wait_until_page_contains_element(self, locator, timeout=None):
        return await self._wait_for_selenium_selector(locator, timeout, visible=True, hidden=False)

    async def wait_until_element_is_hidden(self, locator, timeout=None):
        raise Exception('Not implemented.')

    async def wait_until_element_is_visible(self, locator, timeout=None):
        raise Exception('Not implemented.')

    async def wait_until_page_contains(self, text, timeout=None):
        locator = "xpath://*[contains(., %s)]" % self.escape_xpath_value(text)
        return await self._wait_for_selenium_selector(locator, timeout, visible=True, hidden=False)

    async def wait_until_page_does_not_contains(self, text, timeout=None):
        raise Exception('Not implemented.')

    async def wait_until_element_contains(self, locator, text, timeout=None):
        raise Exception('Not implemented.')

    async def wait_until_element_does_not_contains(self, locator, text, timeout=None):
        raise Exception('Not implemented.')

    async def wait_until_location_contains(self, expected, timeout=None):
        raise Exception('Not implemented.')

    async def wait_until_location_does_not_contains(self, expected, timeout=None):
        raise Exception('Not implemented.')

    async def wait_until_element_is_enabled(self, locator, timeout=None):
        raise Exception('Not implemented.')

    async def wait_until_element_finished_animating(self, locator, timeout=None):
        raise Exception('Not implemented.')

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
