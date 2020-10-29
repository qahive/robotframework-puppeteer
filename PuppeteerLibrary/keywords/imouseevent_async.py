from PuppeteerLibrary.keywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iMouseEventAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def mouse_over(self, locator):
        pass

    @abstractmethod
    async def mouse_down(self, locator):
        pass
    
    @abstractmethod
    async def mouse_up(self):
        pass

    @abstractmethod
    def mouse_move(self, x, y):
        pass
    