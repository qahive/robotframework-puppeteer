from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext
from abc import ABC, abstractmethod

class iPuppeteerLibrary(ABC):

    @abstractmethod
    def get_current_library_context(self) -> iLibraryContext:
        pass

    @abstractmethod
    def create_library_context(self,alias: str, browser_type: str) -> iLibraryContext:
        pass
