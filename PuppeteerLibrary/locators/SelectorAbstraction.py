from PuppeteerLibrary.locators import LocatorParserImplementation
from PuppeteerLibrary.locators import CssLocatorParser, LinkLocatorParser, PartialLinkLocatorParser
from PuppeteerLibrary.locators import IdLocatorParser
from PuppeteerLibrary.locators import XPathLocatorParser
import re


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
        if selector_type == 'xpath' or selector_type == 'partial link':
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
        elif selector_type == 'link':
            return LinkLocatorParser()
        elif selector_type == 'partial link':
            return PartialLinkLocatorParser()
        else:
            raise Exception('Not support selector ' + selector_type)

    @staticmethod
    def _get_selector_pair(selenium_selector: str):
        parser_regexp_types = ['^id', '^xpath', '^css', '^link', '^partial link']
        for parser_regexp in parser_regexp_types:
            match_obj = re.match('('+parser_regexp+')[=:](.*)', selenium_selector)
            if match_obj:
                selector_pair = [None] * 2
                selector_pair[0] = match_obj[1]         # Strategy
                selector_pair[1] = match_obj[2].strip() # Locator value
                return selector_pair
        raise Exception('Selector not valid: ' + selenium_selector)
