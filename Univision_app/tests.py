from django.test import TestCase, Client
from Univision_app.models import User
from Univision_app.forms import SignUpForm
import datetime

class UserTestCase(TestCase):
    
    def setUp(self):
        User.objects.create(name='Tony the Tiger', email='tony@tony.com', datecreated=datetime.datetime.now())
	User.objects.create(name='Zed', email='a@a.com', datecreated=datetime.datetime.now())

    def test_DB_access(self):
        """
	Testing database entry and retrieval
        """
	tony = User.objects.filter(email='tony@tony.com')
	self.assertEqual('Tony the Tiger', tony[0].name)

    def test_sort(self):
	"""
	Testing sorting DB objects
	"""
	sort = User.objects.all().order_by('email')
	self.assertEqual('a@a.com', sort[0].email)

	sort = sort.order_by('name')
	self.assertEqual('Tony the Tiger', sort[0].name)

    def test_urls(self):
	"""
	Testing URLs are working properly
	"""
	client = Client()
	response = client.get('/asdghas')
	self.assertEqual(response.status_code, 404)
	
	response = client.get('/')
	self.assertEqual(response.status_code, 200)
	
	response = client.get('/users/')
	self.assertEqual(response.status_code, 200)

	response = client.get('/users/name/')
	self.assertEqual(response.status_code, 200)

	response = client.get('/users/email/')
	self.assertEqual(response.status_code, 200)

	response = client.get('/admin/')
	self.assertEqual(response.status_code, 302) #/admin/ routes you to the login page


    def test_form(self):
	form_data = {'name': 'Unicorn', 'email':'unicorn@unicorn.com'}
	form = SignUpForm(data=form_data)
	self.assertTrue(form.is_valid())
	
	form_data = {'name':'', 'email':''}
	form = SignUpForm(data=form_data)
	self.assertTrue(not form.is_valid())

