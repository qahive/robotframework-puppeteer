from PuppeteerLibrary.locators.LocatorParserImplementation import LocatorParserImplementation


class CssLocatorParser(LocatorParserImplementation):

    # Parse selenium strategy syntax
    # Example: css:div.main
    def parse(self, strategy_value: str) -> str:
        return strategy_value
