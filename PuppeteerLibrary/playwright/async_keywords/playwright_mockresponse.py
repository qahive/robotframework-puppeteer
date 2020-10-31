import asyncio
import re
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.ikeywords.imockresponse_async import iMockResponseAsync


class PlaywrightMockResponse(iMockResponseAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def mock_current_page_api_response(self, url, mock_response, method='GET', body=None):
        page = self.library_ctx.get_current_page().get_page()
        await page.route(url, lambda route, request: asyncio.ensure_future(self.mock_api_response(route, request, mock_response, method, body)))

    async def mock_api_response(self, route, request,  mock_response, method, body):
        try:
            pos_data = (await request.postData())
        except:
            pos_data = ''
        if body is None or re.search(body, pos_data.replace('\n', '')):
            await route.fulfill(
                **mock_response
            )
        await request.continue_()
        