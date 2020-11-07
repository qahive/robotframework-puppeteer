from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iCheckboxAsync(BaseAsyncKeywords, ABC):

    @abstractmethod
    async def select_checkbox(self, locator):
        pass 

    @abstractmethod
    async def unselect_checkbox(self, locator):
        pass

    @abstractmethod
    async def checkbox_should_be_selected(self, locator):
        pass
    
    @abstractmethod
    async def checkbox_should_not_be_selected(self, locator):
        pass