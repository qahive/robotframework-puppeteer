from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.dropdown_async import DropdownKeywordsAsync
from PuppeteerLibrary.keywords.idropdown_async import iDropdownAsync


class DropdownKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)
        self.async_func = DropdownKeywordsAsync(self.ctx)

    def get_async_keyword_group(self) -> iDropdownAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def select_from_list_by_value(self, locator, values):
        return self.loop.run_until_complete(self.get_async_keyword_group().select_from_list_by_value(locator, values))
        # return self.loop.run_until_complete(self.async_func.select_from_list_by_value_async(locator, values))

    @keyword
    def select_from_list_by_label(self, locator, labels):
        return self.loop.run_until_complete(self.get_async_keyword_group().select_from_list_by_label(locator, labels))
        # return self.loop.run_until_complete(self.async_func.select_from_list_by_label_async(locator, labels))
