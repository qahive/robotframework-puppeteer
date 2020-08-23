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
