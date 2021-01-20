from PuppeteerLibrary.ikeywords.idropdown_async import iDropdownAsync
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction


class PuppeteerDropdown(iDropdownAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def select_from_list_by_value(self, locator, values):
        await self.library_ctx.get_current_page().select_with_selenium_locator(locator, values)

    async def select_from_list_by_label(self, locator, labels):
        evaluate = ''
        selector_value = SelectorAbstraction.get_selector(locator)
        if SelectorAbstraction.is_xpath(locator):
            evaluate = '''
                element = document.evaluate('{selector_value}//option[text()=\"{label}\"]', document, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, label=labels)
        else:
            evaluate = '''
                selector_element = document.querySelector('{selector_value}');
                element = document.evaluate('//option[text()=\"{label}\"]', selector_element, null, XPathResult.ANY_TYPE, null).iterateNext();
                element.selected = true;
            '''.format(selector_value=selector_value, label=labels)
        return await self.library_ctx.get_current_page().evaluate_with_selenium_locator(evaluate)

    async def get_selected_list_labels(self, locator: str) -> str:
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        options = await element.querySelectorAll('option:checked')
        selected_labels = []
        for option in options:
            selected_labels.append((await (await option.getProperty('textContent')).jsonValue()))
        return selected_labels

    async def get_list_labels(self, locator: str) -> str:
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        options = await element.querySelectorAll('option')
        selected_labels = []
        for option in options:
            selected_labels.append((await (await option.getProperty('textContent')).jsonValue()))
        return selected_labels

    async def get_selected_list_values(self, locator: str) -> str:
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        options = await element.querySelectorAll('option:checked')
        selected_labels = []
        for option in options:
            selected_labels.append((await (await option.getProperty('value')).jsonValue()))
        return selected_labels

    async def get_list_values(self, locator: str) -> str:
        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
        options = await element.querySelectorAll('option')
        selected_labels = []
        for option in options:
            selected_labels.append((await (await option.getProperty('value')).jsonValue()))
        return selected_labels
