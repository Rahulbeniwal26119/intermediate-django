from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView
# Create your tests here.


class HomePageTests(TestCase):
    
    def setUp(self) -> None:
        self.url = reverse("homepage")
        self.response = self.client.get(self.url)

    def test_url_exists(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_home_page_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_name_used(self):
        self.assertTemplateUsed(self.response, "home.html")
    
    def test_title(self):
        self.assertContains(self.response, "home")
    
    def test_body(self):
        self.assertNotContains(self.response, "This is my pages")
    
    def test_resolve_view(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(TestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)
    
    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_about_page_content_template(self):
        self.assertTemplateUsed(self.response, "about.html")
    
    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "About Page")
    
    def test_about_page_view(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
