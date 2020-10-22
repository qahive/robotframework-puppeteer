from PuppeteerLibrary.keywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iDropdownAsync(BaseAsyncKeywords, ABC):

    @abstractmethod
    async def select_from_list_by_value(self, locator, values):
        pass

    @abstractmethod
    async def select_from_list_by_label(self, locator, labels):
        pass
