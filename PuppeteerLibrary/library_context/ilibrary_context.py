from abc import ABC, abstractmethod


class iLibraryContext(ABC):

    browser_type: str = None
    timeout: int = 30

    def __init__(self, browser_type: str):
        self.browser_type = browser_type
    
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
    async def create_new_page(self, options: dict=None):
        pass

    @abstractmethod
    def get_current_page(self):
        pass

    @abstractmethod
    async def get_all_pages(self):
        pass

    @abstractmethod
    async def close_browser_context(self):
        pass

    @abstractmethod
    def get_async_keyword_group(self, keyword_group_name: str):
        pass
