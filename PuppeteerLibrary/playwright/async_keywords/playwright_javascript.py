from PuppeteerLibrary.ikeywords.ijavascript_async import iJavascriptAsync
from PuppeteerLibrary.utils.coverter import str2str


class PlaywrightJavascript(iJavascriptAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    async def execute_javascript(self, code):
        code = str2str(code)
        return await self.library_ctx.get_current_page().get_page().evaluate(code)
