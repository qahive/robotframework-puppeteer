from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iScreenshotAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def capture_page_screenshot(self, path: str):
        pass
    
    