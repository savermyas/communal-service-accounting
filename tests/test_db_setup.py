from django.test import TestCase
from commapp.models import UserEntity
from commapp.models import Counter
from commapp.models import ServiceProviderEntity
from commapp.models import ServiceProvider
from commapp.models import Apartment
from commapp.models import User

class DBSetupTestCase(TestCase):

    def setUp(self):
        service_provider_entity_1 = ServiceProviderEntity(
            name="Gorvodokanal",
            url="http://gvc.ru",
        )
        service_provider_entity_2 = ServiceProviderEntity(
            name="Pertoelectrosbyt",
            url="http://pes.spb.ru",
        )
        service_provider_entity_1.save()
        service_provider_entity_2.save()

        service_provider_1 = ServiceProvider(
            username="water1",
            password="mypassw#NW",
            service_provider=service_provider_entity_1
        )

        service_provider_2 = ServiceProvider(
            username="pes",
            password="pespassWwd",
            service_provider=service_provider_entity_2
        )

        service_provider_1.save()
        service_provider_2.save()

        user_entity = UserEntity(name="testuser")
        user_entity.save()

        apartment = Apartment(

        )

        for x in range(0, 10):
            counter = Counter(name="{x}{x}{x}{x}{x}{x}".format(x=x),
                               info="Counter #{}".format(x),
                               previous_value=x,
                               current_value=2*x+10)
            counter.save()
            if x % 2 == 0:
                service_provider_1.counters.add(counter)
            else:
                service_provider_2.counters.add(counter)


