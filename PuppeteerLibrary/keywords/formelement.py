from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.formelement_async import FormElementKeywordsAsync


class FormElementKeywords(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.async_func = FormElementKeywordsAsync(self.ctx)

    @keyword
    def input_text(self, selenium_locator, text, clear=True):
        self.loop.run_until_complete(self.async_func.input_text_async(selenium_locator, text, clear))

    @keyword
    def clear_element_text(self, selenium_locator):
        self.loop.run_until_complete(self.async_func.clear_element_text_async(selenium_locator))

