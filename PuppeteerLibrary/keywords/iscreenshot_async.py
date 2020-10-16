from PuppeteerLibrary.keywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iScreenshotAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def capture_page_screenshot(self, path: str):
        pass
    
    