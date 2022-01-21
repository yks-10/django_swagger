from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import *
from train import views 

class TestTrain(TestCase):
	@classmethod 
	def setUpTestData(cls):
		testuser1 = User.objects.create_user(username='testuser1', password='abc123')
		testuser1.save()

		test_post=Train.objects.create(train_name='testname', train_no='trainnumber', starting_at='startingpoint', ending_at='ending_point', d_date='ending date')
		test_post.save()

	def test_blog_content(self):
		post=T.objects.get(id=1)
		train_name = f'{ post.train_name}'
		train_no = f'{post.train_no}'
		starting_at = f'{post.starting_at}'
		ending_at = f'{post.ending_at}'
		d_date = f'{post.d_date}'
		self.assertEqual(train_name,'VAIGAII')
		self.assertEqual(train_no, '12012')
		self.assertEqual(starting_at, 'chennai')
		self.assertEqual(ending_at, 'madurai')
		self.assertEqual(d_date, '2021-12-25T05:37:00s')
		
'''	def setUp(self):
		self.client = APIClient()
		#self.factory = APIRequestFactory()
		self.view = views.TrainViewSet.as_view({'get':'list'})
		self.uri = '/train/'
	@staticmethod
	def setup_user(): 
		User = get_user_model()
		return User.objects.create_user(
			'test',
			email='testuser@test.com',
			password='test'
		)

	def test_list(self):
		self.client.login(username="test", password="test")
		response = self.client.get(self.uri)
		self.assertEqual(response.status_code,200,'Expected Response Code 200, received {0} instead.'.format(response.status_code))'''
