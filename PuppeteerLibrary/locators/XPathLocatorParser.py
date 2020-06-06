from PuppeteerLibrary.locators.LocatorParserImplementation import LocatorParserImplementation


class XPathLocatorParser(LocatorParserImplementation):

    # Parse selenium strategy syntax
    # Example: xpath://div, xpath=//div
    def parse(self, strategy_value: str) -> str:
        return ''+strategy_value
