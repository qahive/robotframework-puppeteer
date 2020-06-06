from abc import ABC, abstractmethod


class LocatorParserImplementation(ABC):

    @abstractmethod
    def parse(self, strategy_value: str) -> str:
        pass
