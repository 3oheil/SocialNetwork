from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# Create your tests here.

class friendshipTests(SimpleTestCase):
    def url_in_user_list_view_exist(self):
        response = self.client.get('list/')
        self.assertEqual(response.status_code, 200)

    def url_name_in_user_list_view_exist(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)

    def url_in_request_view_exist(self):
        response = self.client.get('request/')
        self.assertEqual(response.status_code, 200)

    def url_name_in_request_view_exist(self):
        response = self.client.get(reverse('request'))
        self.assertEqual(response.status_code, 200)

    def url_in_request_list_view_exist(self):
        response = self.client.get('request-list')
        self.assertEqual(response.status_code, 200)

    def url_name_in_request_list_view_exist(self):
        response = self.client.get(reverse('request_list'))
        self.assertEqual(response.status_code, 200)

    def url_in_accept_view_exist(self):
        response = self.client.get('accept')
        self.assertEqual(response.status_code, 200)

    def url_name_in_accept_view_exist(self):
        response = self.client.get(reverse('accepted'))
        self.assertEqual(response.status_code, 200)

    def url_in_friend_list_view_exist(self):
        response = self.client.get('friends')
        self.assertEqual(response.status_code, 200)

    def url_name_in_friend_list_view_exist(self):
        response = self.client.get(reverse('friends_list'))
        self.assertEqual(response.status_code, 200)
