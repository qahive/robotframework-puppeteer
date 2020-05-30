from PuppeteerLibrary.locators import LocatorParserImplementation


class SelectorAbstraction:

    def __init__(self, implementation: LocatorParserImplementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")
    