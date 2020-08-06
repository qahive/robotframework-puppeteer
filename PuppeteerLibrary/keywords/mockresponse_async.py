import asyncio

from pyppeteer.network_manager import Request
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class MockResponseKeywordsAsync(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx

    @keyword
    async def mock_current_page_api_response_async(self):
        page = self.ctx.get_current_page()
        await page.setRequestInterception(True)
        page.on('request', lambda request: asyncio.ensure_future(self.mock_api_response(request)))

    async def mock_api_response(self, request: Request):
        await request.respond({
            'status': 200,
            'headers': {
                'foo': 'bar'
            },
            'contentType': 'text/html; charset=UTF-8',
            'body': 'Yo, page!'
        })
        # await request.continue_()
