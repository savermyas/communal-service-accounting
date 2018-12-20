from django.template import Context, Template
from commapp.models import Apartment
from django.test import TestCase


class ApartmentTemplateTestCase(TestCase):

    fixtures = ['fixtures/test.json']

    def test_parse(self):
        with open('tests/data/apartments.html',
                  'r', encoding='utf-8') as myfile:
            template_to_render = Template(myfile.read())

        context = Context(
            {"apartments": [
                apartment for apartment in Apartment.objects.all()
            ]}
        )
        print(template_to_render.render(context))
