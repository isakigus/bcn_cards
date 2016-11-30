from django.test import TestCase, Client
from .views import Documentation, Cards
from .models import Card

client = Client()


class Api(TestCase):
    def test_create_card(self):
        response = self.client.post('/card/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/card/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/card/all/')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/card/1/')
        self.assertEqual(response.status_code, 200)

    def test_create_card_position(self):
        response = self.client.post('/card/')

        self.assertEqual(response.status_code, 200)

        params = {'card_id': 1,
                  'lat': '00,00',
                  'lon': '3,33'}

        response = self.client.post('/card/position', params)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/card/1/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_home(self):
        response = self.client.get('/card/awe4c')
        self.assertEqual(response.status_code, 200)

    def test_get_position(self):
        response = self.client.get('/position/awe4c')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/card/position/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/card/position/1aaaa')
        self.assertEqual(response.status_code, 200)

    def test_post_position(self):
        response = self.client.post('/position/')
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/card/position/')
        self.assertEqual(response.status_code, 200)

    def test_get_documentation(self):
        response = self.client.post('/card/api/info/')
        self.assertEqual(response.status_code, 405)
        response = self.client.get('/card/api/info')
        self.assertEqual(response.status_code, 200)


class TestDocumentation(TestCase):
    def test_parser_doc_string(self):
        doc_string = """ url: /card/(<id>|all)/
            params: id (number)
            description: search a card by <id>, if "all" is used all the cards are displayed
            """
        expected = {'url': ' /card/(<id>|all)/',
                    'params': ' id (number)',
                    'description': ' search a card by <id>, if "all" is used all the cards are displayed'
                    }
        result = Documentation.parser_doc_string(doc_string)
        self.assertEqual(result, expected)

    def test_get_api_strings(self):
        result = Documentation.get_api_strings()
        self.assertTrue(isinstance(result, list))

    def test_is_an_api_method(self):
        self.assertTrue(Documentation.is_an_api_method('get'))
        self.assertFalse(Documentation.is_an_api_method('get_api_strings'))

    def test_is_documented_class(self):
        self.assertFalse(Documentation.is_documented_class(Documentation))
        self.assertTrue(Documentation.is_documented_class(Cards))
