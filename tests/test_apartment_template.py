from django.template import Context, Template
from tests.test_db_setup import DBSetupTestCase

class ApartmentTemplateTestCase(DBSetupTestCase):

    def test_parse(self):
        with open('tests/data/apartments.html',
                  'r', encoding='utf-8') as myfile:
            template_to_render = Template(myfile.read())

#        context = Context({"apartments": self.apartments})
#        print(template_to_render.render(context))
