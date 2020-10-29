from PuppeteerLibrary.keywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iJavascriptAsync(BaseAsyncKeywords, ABC):
    
    @abstractmethod
    async def execute_javascript(self, code):
        pass
