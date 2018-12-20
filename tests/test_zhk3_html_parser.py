from django.test import TestCase
from commapp.zhk3_html_parser import Zhk3HTMLParser


class ZHK3ParserTestCase(TestCase):
    text_data = ""

    def setUp(self):
        with open('tests/data/zhk3_meters.html',
                  'r', encoding='utf-8') as myfile:
            self.text_data = myfile.read()

    def test_parse(self):
        parser = Zhk3HTMLParser()
        rezults = parser.parse_text(self.text_data)
        assert [(rezult.name, rezult.id, rezult.info, rezult.previous_value, rezult.current_value) for rezult in
                rezults] == [
                   ('Отопление.', '80839',
                    '/personal/meters/?type=history&action=get_meters&id=80839',
                    '21.903', '21.903'),
                   ('ХВС водоподведение', '46118',
                    '/personal/meters/?type=history&action=get_meters&id=46118',
                    '108', '117'),
                   ('ХВС водоподвед. для ГВС', '46119',
                    '/personal/meters/?type=history&action=get_meters&id=46119',
                    '67', '74')]
