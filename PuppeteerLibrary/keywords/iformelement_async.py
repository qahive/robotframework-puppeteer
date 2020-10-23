from PuppeteerLibrary.keywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iFormElementAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def input_text(self, locator: str, text: str, clear=True):
        pass
    
    @abstractmethod
    async def clear_element_text(self, locator: str):
        pass
    