from tests.test_db_setup import DBSetupTestCase
from commapp.models import UserEntity
from commapp.models import Counter
from commapp.models import ServiceProviderEntity
from commapp.models import ServiceProvider


class ModelTestCase(DBSetupTestCase):

    def test_user_entity(self):
        assert [user.name for user in UserEntity.objects.all()] == ["testuser"]

    def test_counters(self):
        assert [counter.name for counter in Counter.objects.all()] == \
               ["000000", "111111", "222222", "333333", "444444",
                "555555", "666666", "777777", "888888", "999999"]

    def test_user_entity(self):
        assert [user.name for user in UserEntity.objects.all()] == ["testuser"]

    def test_service_provider_entity(self):
        assert [service_provider_entity.name for service_provider_entity
                in ServiceProviderEntity.objects.all()] == \
               ["Gorvodokanal", "Pertoelectrosbyt"]

    def test_service_providers(self):
        assert [service_provider.name for service_provider
                in ServiceProviderEntity.objects.all()] == \
               ["Gorvodokanal", "Pertoelectrosbyt"]
