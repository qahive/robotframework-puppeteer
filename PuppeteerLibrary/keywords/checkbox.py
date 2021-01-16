from PuppeteerLibrary.ikeywords.icheckbox_async import iCheckboxAsync
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class CheckboxKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iCheckboxAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    @keyword
    def select_checkbox(self, locator):
        """ Select checkbox based on locator
        """
        self.info(f"Select checkbox {locator}.")
        return self.loop.run_until_complete(self.get_async_keyword_group().select_checkbox(locator))

    @keyword
    def unselect_checkbox(self, locator):
        """ Unselect checkbox based on locator
        """
        self.info(f"Unselect checkbox {locator}.")
        return self.loop.run_until_complete(self.get_async_keyword_group().unselect_checkbox(locator))

    @keyword
    def checkbox_should_be_selected(self, locator):
        """ Valicate checkbox should selected
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().checkbox_should_be_selected(locator))

    @keyword
    def checkbox_should_not_be_selected(self, locator):
        """ Valicate checkbox should not be selected
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().checkbox_should_not_be_selected(locator))
