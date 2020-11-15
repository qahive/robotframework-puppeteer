from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iElementAsync(BaseAsyncKeywords, ABC):

    ##############################
    # Query Element
    ##############################
    @abstractmethod
    async def find_elements(self, locator: str):
        pass

    ##############################
    # Action
    ##############################
    @abstractmethod
    async def click_element(self, locator: str, noWaitAfter: str='False'):
        pass

    @abstractmethod
    async def click_link(self, locator: str):
        pass

    @abstractmethod
    async def click_button(self, locator: str):
        pass

    @abstractmethod
    async def click_image(self, locator: str):
        pass

    @abstractmethod
    async def click_element_at_coordinate(self, locator: str, xoffset: str, yoffset: str):
        pass
    
    @abstractmethod
    async def upload_file(self, locator: str, file_path: str):
        pass

    @abstractmethod
    async def press_keys(self, locator: str, *keys: str):
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
    async def get_attribute(self, locator: str, attribute: str) -> str:
        pass
    
    @abstractmethod
    async def element_text_should_be(self, locator: str, expected: str, ignore_case=False):
        pass

    @abstractmethod
    async def element_text_should_not_be(self, locator: str, expected: str, ignore_case=False):
        pass

    ##############################
    # Scrolling
    ##############################
    @abstractmethod
    async def scroll_element_into_view(self, locator: str):
        pass
