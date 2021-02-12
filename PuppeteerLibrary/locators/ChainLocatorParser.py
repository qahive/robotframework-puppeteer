from PuppeteerLibrary.locators.LocatorParserImplementation import LocatorParserImplementation


class ChainLocatorParser(LocatorParserImplementation):

    def parse(self, strategy_value: str) -> str:
        return strategy_value
