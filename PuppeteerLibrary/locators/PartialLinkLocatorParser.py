from PuppeteerLibrary.locators.LocatorParserImplementation import LocatorParserImplementation


class PartialLinkLocatorParser(LocatorParserImplementation):

    def parse(self, strategy_value: str) -> str:
        return f'//a[contains(text()="{strategy_value}")]'
