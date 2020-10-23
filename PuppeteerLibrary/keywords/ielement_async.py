from PuppeteerLibrary.keywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iElementAsync(BaseAsyncKeywords, ABC):

    ##############################
    # Click
    ##############################
    @abstractmethod
    async def click_element(self, locator: str):
        pass

    ##############################
    # Status
    ##############################
    @abstractmethod
    async def element_should_be_enabled(self, locator: str):
        pass

    @abstractmethod
    async def element_should_be_disabled(self, locator: str):
        pass

    @abstractmethod
    async def element_should_be_visible(self, locator:str):
        pass
    
    @abstractmethod
    async def element_should_not_be_visible(self, locator:str):
        pass
    
    ##############################
    # Property
    ##############################
    @abstractmethod
    async def element_should_contain(self, locator: str, expected: str, ignore_case=False):
        pass

    @abstractmethod
    async def element_should_not_contain(self, locator: str, expected: str, ignore_case=False):
        pass

    @abstractmethod
    async def get_text(self, locator: str):
        pass
    
    @abstractmethod
    async def element_text_should_be(self, locator: str, expected: str, ignore_case=False):
        pass

    @abstractmethod
    async def element_text_should_not_be(self, locator: str, expected: str, ignore_case=False):
        pass
