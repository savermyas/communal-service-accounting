from django.test import TestCase
from commapp.zhk3_html_parser import Zhk3HTMLParser


class ZHK3ParserTestCase(TestCase):
    text_data = ""

    def setUp(self):
        with open('tests/data/zhk3_meters.html', 'r', encoding='utf-8') as myfile:
            self.text_data = myfile.read()

    def test_parse(self):
        parser = Zhk3HTMLParser()
        rezults = parser.parse_text(self.text_data)
        assert [vars(rezult) for rezult in rezults] == [
            {'name': 'Отопление.', 'id': '80839',
             'info': '/personal/meters/?type=history&action=get_meters&id=80839',
             'previous_value': '21.903', 'current_value': '21.903'},
            {'name': 'ХВС водоподведение', 'id': '46118',
            'info': '/personal/meters/?type=history&action=get_meters&id=46118',
            'previous_value': '108', 'current_value': '117'},
            {'name': 'ХВС водоподвед. для ГВС', 'id': '46119',
             'info': '/personal/meters/?type=history&action=get_meters&id=46119',
             'previous_value': '67', 'current_value': '74'}]
