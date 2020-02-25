from django.test import TestCase
from django_webtest import WebTest

class SiteLayouTestCase(WebTest):
    def test_layout_links(self):
        response = self.app.get('/')
        print(response.html.a)
        assert 'href="/"' in response.html
