from abc import ABC, abstractmethod
from typing import Any

class BasePage(ABC):

    @abstractmethod
    def get_page(self) -> any:
        pass

    @abstractmethod
    async def goto(self, url: str):
        pass

    @abstractmethod
    async def go_back(self):
        pass

    @abstractmethod
    async def reload_page(self):
        pass

    @abstractmethod
    async def title(self):
        pass
    
    @abstractmethod
    async def set_viewport_size(self, width, height):
        pass

    ############
    # Click
    ############
    @abstractmethod
    async def click(self, selector: str, options: dict = None, **kwargs: Any):
        pass

    @abstractmethod
    async def click_with_selenium_locator(self, selenium_locator: str, options: dict = None, **kwargs: Any):
        pass

    @abstractmethod
    async def click_xpath(self, selector: str, options: dict = None, **kwargs: Any):
        pass

    ############
    # Type
    ############
    @abstractmethod
    async def type_with_selenium_locator(self, selenium_locator: str, text: str, options: dict = None, **kwargs: Any):
        pass

    @abstractmethod
    async def type_xpath(self, selector, text: str, options: dict = None, **kwargs: Any):
        pass

    ############
    # Wait
    ############
    @abstractmethod
    async def waitForSelector_with_selenium_locator(self, selenium_locator: str, timeout: float, visible=False, hidden=False):
        pass

    ############
    # Query
    ############
    @abstractmethod
    async def querySelector(self, selector: str):
        pass

    @abstractmethod
    async def querySelectorAll_with_selenium_locator(self, selenium_locator: str):
        pass

    @abstractmethod
    async def querySelector_with_selenium_locator(self, selenium_locator: str):
        pass
