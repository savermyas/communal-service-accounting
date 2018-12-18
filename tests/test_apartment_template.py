from django.test import TestCase
from commapp.apartment import Apartment
from commapp.counter import Counter
from commapp.serviceprovider import ServiceProvider


class ApartmentTemplateTestCase(TestCase):
    counter1_1 = Counter(
        name="Cold water",
        id="111111",
        info="Counter 1 Apt 1",
        previous_value=1000,
        current_value=2000
    )
    counter1_2 = Counter(
        name="Hot water",
        id="111112",
        info="Counter 2 Apt 1",
        previous_value=1024,
        current_value=2048
    )
    service_provider_1_1 = ServiceProvider(
        name="Gorvodokanal",
        url="http://gvc.ru",
        counters=[counter1_1, counter1_2]
    )
    counter1_3 = Counter(
        name="Electricity day",
        id="555555",
        info="Counter 3 Apt 1",
        previous_value=1000,
        current_value=2000
    )
    counter1_4 = Counter(
        name="Electricity night",
        id="666666",
        info="Counter 4 Apt 1",
        previous_value=1024,
        current_value=2048
    )
    service_provider_1_2 = ServiceProvider(
        name="Pertoelectrosbyt",
        url="http://pes.spb.ru",
        counters=[counter1_3, counter1_4]
    )
    apartments = [
        Apartment(
            [service_provider_1_1, service_provider_1_2]
        )
    ]

    def test_parse(self):
        flat_sp = []
        for apt in self.apartments:
            for sp in apt.service_providers:
                flat_sp.append(sp)

        print([vars(sp) for sp in flat_sp])
