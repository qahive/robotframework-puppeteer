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
        self.info(
            f"Selecting options from selection list '{locator}' by "
            f"value {', '.join(values)}."
        )
        return self.loop.run_until_complete(self.get_async_keyword_group().select_from_list_by_value(locator, values))

    @keyword
    def select_from_list_by_label(self, locator, labels):
        self.info(
            f"Selecting options from selection list '{locator}' by "
            f"label {', '.join(labels)}."
        )
        return self.loop.run_until_complete(self.get_async_keyword_group().select_from_list_by_label(locator, labels))

    @keyword
    def get_selected_list_label(self, locator):
        """ Return the label of selected option from element.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_selected_list_labels(locator))[0]

    @keyword
    def get_selected_list_labels(self, locator):
        """ Return the label list of selected options from element.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_selected_list_labels(locator))

    @keyword
    def get_list_labels(self, locator):
        """ Return the label list of options from element.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_list_labels(locator))

    @keyword
    def get_selected_list_value(self, locator):
        """ Return the value of selected option from element.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_selected_list_values(locator))[0]


    @keyword
    def get_selected_list_values(self, locator):
        """ Return the value list of selected options from element.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_selected_list_values(locator))

    @keyword
    def get_list_values(self, locator):
        """ Return the value list of options from element.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_list_values(locator))

