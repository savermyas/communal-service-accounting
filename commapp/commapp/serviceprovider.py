from abc import abstractmethod


class ServiceProvider(object):

    def __init__(self,
                 name="ProviderName",
                 url="http://provider.com",
                 counters=[]):
        self.name = name
        self.url = url
        self.counters = counters

    @abstractmethod
    def fetch_remote_data(self):
        return None
