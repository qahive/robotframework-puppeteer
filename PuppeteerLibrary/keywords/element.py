from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.keywords.element_async import ElementKeywordsAsync


class ElementKeywords(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx
        self.async_func = ElementKeywordsAsync(self.ctx)

    @keyword
    def click_element(self, locator):
        """Clicks element identified by ``locator``.

        Example:

        | `Click Element`                                  | id:register          |
        """
        return self.loop.run_until_complete(self.async_func.click_element_async(locator))

    @keyword
    def click_link(self, locator):
        """Clicks link identified by ``locator``.

        Example:

        | `Click Link`                                  | id:view_more          |
        """
        return self.loop.run_until_complete(self.async_func.click_link_async(locator))

    @keyword
    def click_button(self, locator):
        """Clicks button identified by ``locator``.

        Example:

        | `Click Button`                                | id:submit          |
        """
        self.loop.run_until_complete(self.async_func.click_button_async(locator))

    @keyword
    def click_image(self, locator):
        """Clicks image identified by ``locator``.

        Example:

        | `Click Image`                                 | id:cat_image          |
        """
        self.loop.run_until_complete(self.async_func.click_image_async(locator))

    @keyword
    def get_text(self, locator):
        """Returns text value of element identified by ``locator``.

        Example:

        | ${text}                                    | `Get Text`          | id:username |
        """
        return self.loop.run_until_complete(self.async_func.get_text_async(locator))

    @keyword
    def get_value(self, locator):
        """Returns specific attribute value of element identified by ``locator``.

        Example:

        | ${value}                                    | `Get Value`          | id:comment |
        """
        return self.loop.run_until_complete(self.async_func.get_text_async(locator))
