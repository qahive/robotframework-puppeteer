from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iMockResponseAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def mock_current_page_api_response(self, url, mock_response, method='GET', body=None):
        pass
