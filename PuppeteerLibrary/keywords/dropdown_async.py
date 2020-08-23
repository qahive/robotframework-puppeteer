from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.locators import SelectorAbstraction


class DropdownKeywordsAsync(LibraryComponent):

    @keyword
    async def select_from_list_by_value_async(self, selenium_locator, values):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self.ctx.get_current_page().evaluate('''
                element = document.evaluate('{selector_value}//option[contains(@value, "{values}")]', document, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, values=values))
        else:
            await self.ctx.get_current_page().select(selector_value, values)

    @keyword
    async def select_from_list_by_label_async(self, selenium_locator, labels):
        selector_value = SelectorAbstraction.get_selector(selenium_locator)
        if SelectorAbstraction.is_xpath(selenium_locator):
            await self.ctx.get_current_page().evaluate('''
                element = document.evaluate('{selector_value}//option[text()=\"{label}\"]', document, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, label=labels))
        else:
            await self.ctx.get_current_page().evaluate('''
                selector_element = document.querySelector('{selector_value}');
                element = document.evaluate('//option[text()=\"{label}\"]', selector_element, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, label=labels))
