from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iDropdownAsync(BaseAsyncKeywords, ABC):

    @abstractmethod
    async def select_from_list_by_value(self, locator, values):
        pass

    @abstractmethod
    async def select_from_list_by_label(self, locator, labels):
        pass

    @abstractmethod
    async def get_selected_list_labels(self, locator: str) -> str:
        pass

    @abstractmethod
    async def get_list_labels(self, locator: str) -> str:
        pass

    @abstractmethod
    async def get_selected_list_values(self, locator: str) -> str:
        pass

    @abstractmethod
    async def get_list_values(self, locator: str) -> str:
        pass
