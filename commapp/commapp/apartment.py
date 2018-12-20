class Apartment(object):
    def __init__(self,
                 name="",
                 address="",
                 service_providers=[]):
        self.name = name
        self.address = address
        self.service_providers = service_providers
