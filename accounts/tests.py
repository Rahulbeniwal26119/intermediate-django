from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView

class CustomUserTestCase(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Rahul",
            email="rahul@moveeasy.com",
            password="test"
        )
        self.assertEqual(user.username, "Rahul")
        self.assertEqual(user.email, "rahul@moveeasy.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.__class__.objects.count(), 1)

    def test_create_super_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="Rahul",
            email="rahul@moveeasy.com",
            password="test_user",
            is_superuser=True,
        )
        self.assertEqual(user.username, "Rahul")
        self.assertEqual(user.email, "rahul@moveeasy.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.__class__.objects.count(), 1)


class SignUpUserTest(TestCase):
    def setUp(self) -> None:
        url = reverse("signup")
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Sign Up")
        self.assertTemplateUsed(self.response, "registration/signup.html")
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")
    
    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
