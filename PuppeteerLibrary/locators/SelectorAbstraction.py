from PuppeteerLibrary.locators import LocatorParserImplementation
from PuppeteerLibrary.locators import CssLocatorParser
from PuppeteerLibrary.locators import IdLocatorParser
from PuppeteerLibrary.locators import XPathLocatorParser


class SelectorAbstraction:

    @staticmethod
    def get_selector(selenium_selector: str) -> str:
        selector_pair = SelectorAbstraction._get_selector_pair(selenium_selector)
        selector_type = selector_pair[0]
        selector_value = selector_pair[1]
        parser = SelectorAbstraction._get_locator_parser(selector_type)
        return parser.parse(selector_value)

    @staticmethod
    def is_xpath(selenium_selector: str) -> bool:
        selector_type = SelectorAbstraction._get_selector_pair(selenium_selector)[0]
        if selector_type == 'xpath':
            return True
        else:
            return False

    @staticmethod
    def _get_locator_parser(selector_type: str) -> LocatorParserImplementation:
        if selector_type == 'id':
            return IdLocatorParser()
        elif selector_type == 'xpath':
            return XPathLocatorParser()
        elif selector_type == 'css':
            return CssLocatorParser()
        else:
            raise Exception('Not support selector ' + selector_type)

    @staticmethod
    def _get_selector_pair(selenium_selector: str):
        selector_pair = selenium_selector.split('=', 1)
        if len(selector_pair) != 2:
            selector_pair = selenium_selector.split(':', 1)
        if len(selector_pair) != 2:
            raise Exception('selector not valid ' + selenium_selector)
        selector_pair[0] = selector_pair[0].lower().strip()
        selector_pair[1] = selector_pair[1].strip()
        return selector_pair
