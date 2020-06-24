from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.element_async import ElementKeywordsAsync


class ElementKeywords(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.async_func = ElementKeywordsAsync(self.ctx)

    @keyword
    def click_element(self, selenium_locator):
        return self.loop.run_until_complete(self.async_func.click_element_async(selenium_locator))

    @keyword
    def click_link(self, selenium_locator):
        return self.loop.run_until_complete(self.async_func.click_link_async(selenium_locator))

    @keyword
    def click_button(self, selenium_locator):
        self.loop.run_until_complete(self.async_func.click_button_async(selenium_locator))

    @keyword
    def click_image(self, selenium_locator):
        self.loop.run_until_complete(self.async_func.click_image_async(selenium_locator))

    @keyword
    def get_text(self, selenium_locator):
        return self.loop.run_until_complete(self.async_func.get_text_async())

    @keyword
    def get_value(self, selenium_locator):
        return self.loop.run_until_complete(self.async_func.get_text_async())
