from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords

DEFAULT_FILENAME_PAGE = 'puppeteer-screenshot-{index}.png'

class iScreenshotAsync(BaseAsyncKeywords, ABC):

    @abstractmethod
    async def capture_page_screenshot(self, path: str, fullPage: bool):
        pass
    
    