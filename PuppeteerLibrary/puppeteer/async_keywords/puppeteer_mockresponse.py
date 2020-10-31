import asyncio
import re
from pyppeteer.network_manager import Request
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.ikeywords.imockresponse_async import iMockResponseAsync


class PuppeteerMockResponse(iMockResponseAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def mock_current_page_api_response(self, url, mock_response, method='GET', body=None):
        page = self.library_ctx.get_current_page().get_page()
        await page.setRequestInterception(True)
        page.on('request', lambda request:
            asyncio.ensure_future(self.mock_api_response(request, url, mock_response, method, body)))

    async def mock_api_response(self, request: Request, url, mock_response, method, body):
        if re.search(re.escape(url), request.url) is not None and request.method == method:
            try:
                pos_data = (await request.postData())
            except:
                pos_data = ''
            if body is None or re.search(body, pos_data.replace('\n', '')):
                return await request.respond(mock_response)
        await request.continue_()
