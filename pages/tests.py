from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class AboutPageTests(SimpleTestCase):
    def setUp(self):

        self.response = self.client.get(reverse('pages:about'))

    def test_url_about(self):
        self.assertEqual(self.response.status_code, 200)

    def test_html_about(self):
        self.assertTemplateUsed(
            self.response, 
            'pages/about.html'
            )
        self.assertContains(
            self.response, 
            'Aplicación para el control de combustible y gestión de flotas.'
            )
        self.assertNotContains(
            self.response, 
            'Incorrect Content'
            )

    # def test_about_page_status_code(self):
    #     response = self.client.get(self.response)
    #     self.assertEqual(response.status_code, 200)

    # def test_about_page_template(self):
    #     response = self.client.get(self.response)
    #     self.assertEqual(response.status_code, 200)

    # def test_about_page_content_html(self):
    #     response = self.client.get(self.response)
    #     self.assertContains(response, 'Aplicación para el control de combustible y gestión de flotas.')

    # def test_about_page_does_not_contain_incorrect_html(self):
    #     response = self.client.get(self.response)
    #     self.assertNotContains(response, 'Incorrect Content')

    
    
