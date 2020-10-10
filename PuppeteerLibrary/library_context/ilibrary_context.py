from abc import ABC, abstractmethod


class iLibraryContext(ABC):

    browser_type: str = None

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

