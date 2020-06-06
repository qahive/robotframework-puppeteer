from PuppeteerLibrary.locators import LocatorParserImplementation
from PuppeteerLibrary.locators import CssLocatorParser
from PuppeteerLibrary.locators import IdLocatorParser
from PuppeteerLibrary.locators import XPathLocatorParser


class SelectorAbstraction:

    @staticmethod
    def get_selector(selenium_selector: str) -> str:
        selector_pair = selenium_selector.split('=', 1)
        if len(selector_pair) != 2:
            selector_pair = selenium_selector.split(':', 1)
        if len(selector_pair) != 2:
            raise Exception('selector not valid '+selenium_selector)
        selector_type = selector_pair[0].lower().strip()
        selector_value = selector_pair[1].strip()
        parser = SelectorAbstraction._get_locator_parser(selector_type)
        return parser.parse(selector_value)

    @staticmethod
    def _get_locator_parser(selector_type: str) -> LocatorParserImplementation:
        selector_type = selector_type
        if selector_type == 'id':
            return IdLocatorParser()
        elif selector_type == 'xpath':
            return XPathLocatorParser()
        elif selector_type == 'css':
            return CssLocatorParser()
        else:
            raise Exception('not support selector ' + selector_type)
