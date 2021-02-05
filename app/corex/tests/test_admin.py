from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTestes(TestCase):

    # Previous from doing the tests
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@ii40services.com',
            password='password123'
        )
        # Helper function of log in the user to django admin
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@ii40services.com',
            password='password123',
            name='Test user full name'
        )

    def test_user_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:corex_user_changelist')  # Dynamic admin url
        res = self.client.get(url)  # HTTP Get

        # look into the actual object and check for the contenst there
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page workd"""
        # /admin/corex/user/
        url = reverse('admin:corex_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:corex_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
