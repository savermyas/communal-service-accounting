from django.test import TestCase
from commapp.zhk3_html_parser import Zhk3HTMLParser

class ZHK3ParserTestCase(TestCase):
    text_data = ""

    def setUp(self):
        with open('tests/data/zhk3_meters.html', 'r') as myfile:
            self.text_data = myfile.read()

    def test_parse(self):
        parser = Zhk3HTMLParser()
        rezults = parser.parse_text(self.text_data)
        assert [ rezult.id for rezult in rezults ] == ["80839", "46118", "46119"]
