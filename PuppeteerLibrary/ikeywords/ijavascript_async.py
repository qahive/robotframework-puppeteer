from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iJavascriptAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def execute_javascript(self, code):
        pass
