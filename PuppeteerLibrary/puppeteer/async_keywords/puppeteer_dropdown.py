from PuppeteerLibrary.keywords.idropdown_async import iDropdownAsync
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction


class PuppeteerDropdown(iDropdownAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def select_from_list_by_value(self, locator, values):
        selector_value = SelectorAbstraction.get_selector(locator)
        if SelectorAbstraction.is_xpath(locator):
            await self.library_ctx.get_current_page().get_page().evaluate('''
                element = document.evaluate('{selector_value}//option[contains(@value, "{values}")]', document, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, values=values))
        else:
            await self.library_ctx.get_current_page().get_page().select(selector_value, values)

    async def select_from_list_by_label(self, locator, labels):
        selector_value = SelectorAbstraction.get_selector(locator)
        if SelectorAbstraction.is_xpath(locator):
            await self.library_ctx.get_current_page().get_page().evaluate('''
                element = document.evaluate('{selector_value}//option[text()=\"{label}\"]', document, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, label=labels))
        else:
            await self.library_ctx.get_current_page().get_page().evaluate('''
                selector_element = document.querySelector('{selector_value}');
                element = document.evaluate('//option[text()=\"{label}\"]', selector_element, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, label=labels))

