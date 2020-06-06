from PuppeteerLibrary.locators.LocatorParserImplementation import LocatorParserImplementation


class IdLocatorParser(LocatorParserImplementation):

    # Parse selenium strategy syntax
    # Example: id:username, id=username
    def parse(self, strategy_value: str) -> str:
        return f'#{strategy_value}'
