from django.test import TestCase
from commapp.models import UserEntity
from commapp.models import Counters


class ModelTestCase(TestCase):

    def setUp(self):
        user_entity = UserEntity(name="testuser")
        user_entity.save()
        for x in range(0, 10):
            counter = Counters(name="{x}{x}{x}{x}{x}{x}".format(x=x),
                              info="Counter #{}".format(x),
                              previous_value=x,
                              current_value=2*x+10)
            counter.save()

    def test_user_entity(self):
        assert [user.name for user in UserEntity.objects.all()] == ["testuser"]

    def test_counters(self):
        assert [counter.name for counter in Counters.objects.all()] == ["000000", "111111", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999"]

