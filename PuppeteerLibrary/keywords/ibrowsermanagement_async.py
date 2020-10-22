from PuppeteerLibrary.keywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iBrowserManagementAsync(BaseAsyncKeywords, ABC):

    @abstractmethod
    async def maximize_browser_window(self, width=1366, height=768):
        pass

    @abstractmethod
    async def go_to(self, url):
        pass

    @abstractmethod
    async def go_back(self, url):
        pass

    @abstractmethod
    async def reload_page(self):
        pass

    @abstractmethod
    async def get_window_count(self):
        pass
    
    @abstractmethod
    async def wait_for_new_window_open(self, timeout=None):
        pass
    
    @abstractmethod
    async def switch_window(self, locator='MAIN'):
        pass
