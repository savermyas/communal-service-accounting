from abc import abstractmethod


class ServiceProvider(object):
    name = "ProviderName"
    url = "http://provider.com"
    counters = []

    @abstractmethod
    def fetch_remote_data(self):
        return None
