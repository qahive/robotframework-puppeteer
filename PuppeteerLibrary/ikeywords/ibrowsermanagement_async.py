from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


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

    ##############################
    # iFrame
    ##############################
    @abstractmethod
    async def select_frame(self, locator: str):
        pass

    @abstractmethod
    def unselect_iframe(self):
        pass

    ##############################
    # Cookies
    ##############################
    async def get_cookie(self, name: str):
        pass

    async def get_cookies(self):
        pass
    
    async def add_cookie(self, name: str, value: str):
        pass

    async def delete_all_cookies(self):
        pass
