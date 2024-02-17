from django.test import TestCase


class HelloDjangoNCiTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_admin_page(self):
        response = self.client.get("/admin/login/")
        self.assertEqual(200, response.status_code, f'Wrong status code: {response.status_code}')

    def test_about_us_page(self):
        response = self.client.get("/about-us")
        self.assertEqual(200, response.status_code, f'Wrong status code: {response.status_code}')
