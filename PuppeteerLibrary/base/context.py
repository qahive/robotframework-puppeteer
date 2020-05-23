class ContextAware(object):

    def __init__(self, ctx):
        """Base class exposing attributes from the common context.
        :param ctx: The library itself as a context object.
        :type ctx: PuppeteerLibrary.PuppeteerLibrary
        """
        self.ctx = ctx
