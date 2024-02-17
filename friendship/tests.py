from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# Create your tests here.

class FriendshipTests(SimpleTestCase):
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


# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
#
#     def setUp(self):
#         print("setUp: Run once for every test method to set up clean data.")
#         pass
#
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
#
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)
#
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
