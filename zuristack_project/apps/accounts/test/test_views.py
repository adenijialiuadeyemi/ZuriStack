from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import CustomUser

class CustomerUserManagerTests(TestCase):
	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(email='user@email.com', password='foo')
		self.assertEqual(user.email, 'user@email.com')
		
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)
		
		with self.assertRaises(TypeError):
			user.objects.create_user()
		with self.assertRaises(TypeError):
			user.objects.create_user(email='')
		with self.assertRaises(ValueError):
			user.objects.create_user(email='', password='foo')

def test_create_superuser(self):
		User = get_user_model()
		admin_user = User.objects.create_super_user(email='superuser@email.com')
		self.assertEqual(admin_user.email, 'user@email.com')
		
		self.assertTrue(admin_user.is_active),
		self.assertTrue(admin_user.is_staff),
		self.assertTrue(admin_user.is_superuser)
