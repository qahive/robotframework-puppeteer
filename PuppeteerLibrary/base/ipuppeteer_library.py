from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext
from abc import ABC, abstractmethod

class iPuppeteerLibrary(ABC):

    @abstractmethod
    def get_library_context(self, browser_type: str) -> iLibraryContext:
        pass

    
