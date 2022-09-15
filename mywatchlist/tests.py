from django.test import TestCase

# Create your tests here.

def test_url_html(self):
    response = self.get.client('/mywatchlist/html/')
    self.assertEqual(response.status_code, 200)

def test_url_xml(self):
    response = self.get.client('/mywatchlist/xml/')
    self.assertEqual(response.status_code, 200)

def test_url_json(self):
    response = self.get.client('/mywatchlist/json/')
    self.assertEqual(response.status_code, 200)
