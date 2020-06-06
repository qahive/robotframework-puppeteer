from PuppeteerLibrary.locators.LocatorParserImplementation import LocatorParserImplementation


class LinkLocatorParser(LocatorParserImplementation):

    def parse(self, strategy_value: str) -> str:
        return f'//a[text()="{strategy_value}"]'
