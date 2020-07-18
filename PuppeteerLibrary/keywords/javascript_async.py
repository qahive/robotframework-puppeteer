from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent


class JavascriptKeywordsAsync(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx

    @keyword
    async def execute_javascript_async(self, code):
        return await self.ctx.get_current_page().evaluate(code)
