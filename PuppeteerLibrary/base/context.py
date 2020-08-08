import asyncio

class ContextAware(object):

    loop = None

    def __init__(self, ctx):
        """Base class exposing attributes from the common context.
        :param ctx: The library itself as a context object.
        :type ctx: PuppeteerLibrary.PuppeteerLibrary
        """
        try:
            self.loop = asyncio.get_event_loop()
        except:
            print('Warning: Asyncio not supported')
        self.ctx = ctx
        self.ctx.timeout = 30

