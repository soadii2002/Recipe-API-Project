'''
    Tests for models.
'''
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'emailexample.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = [
            ["test1@EXAMPLE.com",  "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email ,expected in email:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_user_without_email_raises_error(self):
        ''' test creating user without email raises error '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', "test123")

    def test_create_superuser(self):
        ''' test creating a superuser '''
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123"
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)