from abc import ABC, abstractmethod
from typing import Any

class BasePage(ABC):

    @abstractmethod
    def get_page(self) -> any:
        pass

    @abstractmethod
    def get_selected_frame_or_page(self) -> any:
        pass

    @abstractmethod
    async def goto(self, url: str):
        pass

    @abstractmethod
    async def go_back(self):
        pass

    @abstractmethod
    async def reload_page(self):
        pass

    @abstractmethod
    async def title(self):
        pass
    
    @abstractmethod
    async def set_viewport_size(self, width, height):
        pass

    ############
    # Click
    ############
    @abstractmethod
    async def click_with_selenium_locator(self, selenium_locator: str, options: dict = None, **kwargs: Any):
        pass

    ############
    # Type
    ############
    @abstractmethod
    async def type_with_selenium_locator(self, selenium_locator: str, text: str, options: dict = None, **kwargs: Any):
        pass

    ############
    # Wait
    ############
    @abstractmethod
    async def waitForSelector_with_selenium_locator(self, selenium_locator: str, timeout: float, visible=False, hidden=False):
        pass

    ##############################
    # Query
    ##############################
    @abstractmethod
    async def querySelectorAll_with_selenium_locator(self, selenium_locator: str):
        pass

    @abstractmethod
    async def querySelector_with_selenium_locator(self, selenium_locator: str):
        pass

    ############
    # Select
    ############
    @abstractmethod
    async def select_with_selenium_locator(self, selenium_locator: str, values: str):
        pass

    ############
    # Evaluate
    ############
    @abstractmethod
    async def evaluate_with_selenium_locator(self, evaluate: str):
        pass

    ##############################
    # iframe
    ##############################
    @abstractmethod
    def set_current_iframe(self, iframe):
        pass

    @abstractmethod
    def unselect_iframe(self):
        pass
