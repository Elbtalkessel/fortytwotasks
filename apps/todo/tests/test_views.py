from django.test import SimpleTestCase
from django.urls import reverse


class IndexViewTest(SimpleTestCase):
    def test_template_used(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")
