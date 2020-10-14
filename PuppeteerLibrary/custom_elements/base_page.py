from abc import ABC, abstractmethod
from typing import Any

class BasePage(ABC):

    @abstractmethod
    def get_page(self) -> any:
        pass

    @abstractmethod
    async def click_with_selenium_locator(self, selenium_locator: str, options: dict = None, **kwargs: Any):
        pass

    @abstractmethod
    async def click_xpath(self, selector: str, options: dict = None, **kwargs: Any):
        pass

    @abstractmethod
    async def click(self, selector: str, options: dict = None, **kwargs: Any):
        pass
