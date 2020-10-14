from PuppeteerLibrary.keywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iElementAsync(BaseAsyncKeywords, ABC):

    @abstractmethod
    async def click_element(self, locator: str):
        pass
