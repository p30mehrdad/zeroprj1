#from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class MessagePageTests(SimpleTestCase): 
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/message/") #test url address
        self.assertEqual(response.status_code,200)
        
    def test_url_availble_by_name(self):
        response = self.client.get(reverse('message')) #name of url in reverse
        self.assertEqual(response.status_code,200)
        
    def test_templates_name(self): 
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response,'home.html') #test by template or 'base.html'
        
    def test_templates_content(self):
        response = self.client.get('/message/') #ba link url
        self.assertContains(response,'<h1>Hi form tehran</h1>') # mohtavaye page ro barasi mikone