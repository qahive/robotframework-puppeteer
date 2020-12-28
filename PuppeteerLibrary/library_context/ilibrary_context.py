import os
from abc import ABC, abstractmethod
from PuppeteerLibrary.custom_elements.base_page import BasePage


class iLibraryContext(ABC):

    browser_type: str = None
    screenshot_path: str = None
    timeout: int = 30

    def __init__(self, browser_type: str):
        self.browser_type = browser_type
        self.screenshot_path = os.curdir
    
    @abstractmethod
    async def start_server(self, options: dict=None):
        pass

    @abstractmethod
    async def stop_server(self):
        pass

    @abstractmethod
    def is_server_started(self) -> bool:
        pass

    @abstractmethod
    async def create_new_page(self, options: dict=None) -> BasePage:
        pass

    @abstractmethod
    def get_current_page(self) -> BasePage:
        pass

    @abstractmethod
    def set_current_page(self, page: any) -> BasePage:
        pass

    @abstractmethod
    async def get_all_pages(self):
        pass

    @abstractmethod
    def get_browser_context(self):
        pass

    @abstractmethod
    async def close_browser_context(self):
        pass

    @abstractmethod
    async def close_window(self):
        pass

    @abstractmethod
    def get_async_keyword_group(self, keyword_group_name: str):
        pass

    def set_screenshot_path(self, path: str):
        self.screenshot_path = path
        if not os.path.exists(self.screenshot_path):
            os.makedirs(self.screenshot_path)

    def get_screenshot_path(self):
        return self.screenshot_path
