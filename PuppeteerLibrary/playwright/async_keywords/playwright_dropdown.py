from PuppeteerLibrary.ikeywords.idropdown_async import iDropdownAsync
from PuppeteerLibrary.locators.SelectorAbstraction import SelectorAbstraction


class PlaywrightDropdown(iDropdownAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def select_from_list_by_value(self, locator, values):
        selector_value = SelectorAbstraction.get_selector(locator)
        return await self.library_ctx.get_current_page().get_selected_frame_or_page().selectOption(selector_value, {
                'value': values
            })

    async def select_from_list_by_label(self, locator, labels):
        selector_value = SelectorAbstraction.get_selector(locator)
        return await self.library_ctx.get_current_page().get_selected_frame_or_page().selectOption(selector_value, {
                'label': labels
            })
        
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