from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from users.forms import CustomUserCreationForm
from .views import RegisterUserView

# Create your tests here.

class CustoUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        # Verify the user was created successfully
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    
    def test_crear_superusuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_superuser(
            username = "testuser",
            email = "testuser@example.com",
            password = "testpassword",
        )
    
        #Qué esperamos
        self.assertEqual(usr.username,"testuser")
        self.assertEqual(usr.email,"testuser@example.com")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)

class RegisterUserTests(TestCase):
    def setUp(self):
        url = reverse('users:register')
        self.response = self.client.get(url)

    def test_template_register(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'users/register.html')
        self.assertContains(self.response, 'Create a new account')
        self.assertNotContains(self.response, 'Login to your account')

    def test_register_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_register_view(self):
        view = resolve('/users/register/')
        self.assertEqual(view.func.__name__, RegisterUserView.as_view().__name__)
