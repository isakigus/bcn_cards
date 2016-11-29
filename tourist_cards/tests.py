import requests

from django.test import TestCase


class CardApi(TestCase):

    def test_create_card(self):

        r = requests.post('http://127.0.0.1:8000/card//')
        print r.content


    def atest_create_card(self):
        r = requests.get('http://127.0.0.1:8001/card/list')
        print r.content
        r = requests.post('http://127.0.0.1:8001/card/')
        print r.content
        r = requests.get('http://127.0.0.1:8001/card/list')
        print r.content
