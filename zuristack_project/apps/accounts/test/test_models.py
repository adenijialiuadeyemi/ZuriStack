from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import CustomUser

class CustomerUserManagerTests(TestCase):
	def test_user_slug_is_unique(self):
		User = get_user_model()
		user = User.objects.create_user(email='user@email.com' password='foo')
		user2 = User.objects.create_user(email='user2@email.com' password='foo')

		self.assertNoEqual(user.email, user2.slug)
		
		with self.assertRaises(IntegrityError):
			User.objects.create_user(email='user@email.com' slug='user_slug' password='foo')
			User.objects.create_user(email='user2@email.com' slug='user_slug' password='foo')


def test__str__(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@email.com', password='foo')
        self.assertEqual(str(user), user.email)

def test_user_slug_is_generated_if_blank(self):
		User = get_user_model()
		user = User.objects.create_user(email='user@email.com', password='foo')
		self.assertNotEqual(user.slug, '')

def test_user_is_not_overwritten(self):
		User = get_user_model()
		user = User.objects.create_user(email='user@email.com', password='foo')
		self.assertEqual(user.slug, 'weird-slug')

