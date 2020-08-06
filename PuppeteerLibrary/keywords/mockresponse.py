from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.keywords.mockresponse_async import MockResponseKeywordsAsync


class MockResponseKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = MockResponseKeywordsAsync(self.ctx)

    @keyword
    def mock_current_page_api_response(self):
        return self.loop.run_until_complete(self.async_func.mock_current_page_api_response_async())
