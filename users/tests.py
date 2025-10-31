from django.test import TestCase
from django.contrib.auth import get_user_model

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
