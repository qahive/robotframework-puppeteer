import abc

class iBrowserManagementAsync:

  @abc.abstractmethod
  async def start_server_async(self, browser="chrome", options: dict = None, **kwargs: any):
    pass

  @abc.abstractmethod
  async def open_browser_async(self, url, browser="chrome", alias = None, options = None):
    pass

  @abc.abstractmethod
  async def close_browser_async(self, alias=None):
    pass

  @abc.abstractmethod
  async def close_all_browser_async(self):
    pass

  @abc.abstractmethod
  async def close_puppeteer_async(self):
    pass
