from rest_framework import serializers 
from .models import Train, Book, Bookedby
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User 
		fields = ('username','email','password')
		extra_kwargs = {'password':{'write_only':True}}

	def create(self, validated_data):
		user = User(
			email = validated_data['email'],
			username = validated_data['username']
		)
		user.set_password(validated_data['password'])
		user.save()
		Token.objects.create(user=user)
		return user


class TSerializer(serializers.ModelSerializer):
	class Meta:
		model = Train 
		fields = '__all__'

class TrainSerializer(serializers.ModelSerializer):
	class Meta:
		model = Train 
		#fields = '__all__'
		fields = ('id','train_name', 'train_no', 'starting_at', 'ending_at')  

class BookSerializer(serializers.ModelSerializer):
	trains = TrainSerializer(many=True, required=False)
	class Meta:
		model = Book
		fields ='__all__'
		#fields = ('train','passenger_name')

class BookedbySerializer(serializers.ModelSerializer):
	books = BookSerializer(many=True, read_only=True, required=False)
	class Meta:
		model = Bookedby 
		fields ='__all__'

