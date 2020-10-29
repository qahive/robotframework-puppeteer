from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iFormElementAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def input_text(self, locator: str, text: str, clear=True):
        pass
    
    @abstractmethod
    async def clear_element_text(self, locator: str):
        pass
    