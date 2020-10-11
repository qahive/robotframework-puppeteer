from typing import List
from PuppeteerLibrary.library_context.ilibrary_context import iLibraryContext
from abc import ABC, abstractmethod

class iPuppeteerLibrary(ABC):

    @abstractmethod
    def get_current_library_context(self) -> iLibraryContext:
        pass

    @abstractmethod
    def get_library_context_by_name(self, alias: str) -> iLibraryContext:
        pass
    
    @abstractmethod
    def get_all_library_context(self) -> List[iLibraryContext]:
        pass

    @abstractmethod
    def create_library_context(self,alias: str, browser_type: str) -> iLibraryContext:
        pass
