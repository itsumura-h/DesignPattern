from django.test import TestCase
from django_webtest import WebTest


class SiteLayouTestCase(WebTest):
    def test_layout_links(self):
        response = self.app.get('/')
        assert '/' in response.html.a['href']
        self.assertEqual(
            len(response.html.findAll('a', href="/")),
            2
        )

        assert response.html.find('a', href="/help/")
        assert response.html.find('a', href="/about/")
        assert response.html.find('a', href="/contact/")
