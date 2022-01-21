from django.db import models
from django.contrib.auth.models import User 

class Train(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	train_name = models.CharField(max_length=40)
	train_no = models.CharField(max_length=6, unique=True)
	starting_at = models.CharField(max_length=30)
	ending_at = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	d_date = models.DateTimeField()
	updated_at = models.DateTimeField(auto_now =True)

	def __str__(self):
		return self.train_name

class Book(models.Model):
	#user= models.ForeignKey(User, on_delete=models.CASCADE)
	train = models.ForeignKey(Train, related_name ='book', on_delete = models.CASCADE)
	passanger_name = models.CharField(max_length=100, unique = True)
   

	def __str__(self):
		return self.passanger_name 

class Bookedby(models.Model):
	book = models.ForeignKey(Book, related_name='Train', on_delete=models.CASCADE)
	train = models.ForeignKey(Train, on_delete=models.CASCADE)
	booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
	#passanger_name = models.CharField(max_length=50)
	#aadhar_no = models.CharField(max_length=12)

	class Meta:
		unique_together = ("train", "booked_by")










