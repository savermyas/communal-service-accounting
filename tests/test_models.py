from tests.test_db_setup import DBSetupTestCase
from commapp.models import User
from commapp.models import UserEntity
from commapp.models import Counter
from commapp.models import ServiceProviderEntity
from commapp.models import ServiceProvider
from commapp.models import Apartment


class ModelTestCase(DBSetupTestCase):

    def test_user_entity(self):
        assert [user.name for user in UserEntity.objects.all()] == ["testuser"]

    def test_counters(self):
        assert [counter.name for counter in Counter.objects.all()] == \
               ["000000", "111111", "222222", "333333", "444444",
                "555555", "666666", "777777", "888888", "999999"]

    def test_service_provider_entity(self):
        assert [service_provider_entity.name for service_provider_entity
                in ServiceProviderEntity.objects.all()] == \
               ["Gorvodokanal", "Pertoelectrosbyt"]

    def test_service_providers(self):
        assert [(service_provider.username, service_provider.password)
                for service_provider in ServiceProvider.objects.all()] == \
               [('water1', 'mypassw#NW'), ('pes', 'pespassWwd')]

    def test_user(self):
        assert [len(user.apartments.all())
                for user in User.objects.all()] == [1]

    def test_apartment(self):
        assert [apartment.name for apartment
                in Apartment.objects.all()] == ["Apartment for rent"]
