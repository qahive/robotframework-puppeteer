from abc import ABC, abstractmethod
from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords


class iBrowserManagementAsync(BaseAsyncKeywords, ABC):

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
    # Trace
    ##############################
    @abstractmethod
    async def start_tracing(self):
        pass

    @abstractmethod
    async def stop_tracing(self, path=None):
        pass

    ##############################
    # Page
    ##############################
    @abstractmethod
    async def set_view_port_size(self, width, height):
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
    
    ##############################
    # State
    ##############################
    async def save_browser_storage_state(self, state_folder: str, ref='user'):
        pass
