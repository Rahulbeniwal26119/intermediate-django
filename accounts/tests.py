from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
# from .forms import CustomUserCreationForm
# from .views import SignupPageView

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
    user_name = "newuser"
    email = "newuser@gmail.com"

    def setUp(self) -> None:
        url = reverse("account_signup")
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Sign Up")
        self.assertTemplateUsed(self.response, "account/signup.html")
    
    def test_signup_form(self):
        get_user_model().objects.create_user(
            self.user_name,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.user_name)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)