import abc

class iBrowserManagement:

  @abc.abstractmethod
  async def open_browser(self, url, browser="chrome", alias=None, options=None):
    pass
