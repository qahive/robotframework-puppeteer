from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.ikeywords.idropdown_async import iDropdownAsync


class DropdownKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iDropdownAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def select_from_list_by_value(self, locator, values):
        return self.loop.run_until_complete(self.get_async_keyword_group().select_from_list_by_value(locator, values))

    @keyword
    def select_from_list_by_label(self, locator, labels):
        return self.loop.run_until_complete(self.get_async_keyword_group().select_from_list_by_label(locator, labels))
