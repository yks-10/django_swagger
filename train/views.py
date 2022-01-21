from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from .models import Train, Book, Bookedby
from .permissions import IsAuthorOrReadOnly
from .serializers import TrainSerializer, TSerializer, BookSerializer, BookedbySerializer, UserSerializer

# Create your views here.


class TrainViewSet(viewsets.ModelViewSet):
	#permission_classes = (permissions.IsAuthenticated,)
	queryset = Train.objects.all()
	serializer_class = TrainSerializer

	def destroy(self, request, *args, **kwargs):
		train = Train.objects.get(pk=self.kwargs["pk"])
		if not request.user == train.created_by:
			raise PermissionDenied("you can not delete this Train.")
		return super().destroy(request, *args, **kwargs)



class TrainList(generics.ListCreateAPIView):
	queryset = Train.objects.all()
	serializer_class = TrainSerializer

class TrainDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = (IsAuthorOrReadOnly,) 
	queryset = Train.objects.all()
	serializer_class = TSerializer
	''' def get(self, request, pk):
			train = get_object_or_404(Train, pk=pk)
			data = TrainSerializer(train).data
			return Response(data)'''

class BookList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = Book.objects.filter(train_id=self.kwargs["pk"])
		#queryset = Book.objects.filter(train_id=self.kwargs["pk"])
		return queryset
		a = Book.objects.all().count()
		print(a)
	serializer_class = BookSerializer 

	
	def post(self, request, *args, **kwargs):
		train = Train.objects.get(pk=self.kwargs["pk"])
		if  request.user == train.created_by:
			raise PermissionDenied("you can not create a train")

		print(*args)
		return super().post(request, *args,**kwargs)


class TrainBook(generics.CreateAPIView):
	serializer_class = BookedbySerializer
	def post(self, request, pk, book_pk):
		booked_by=request.data.get("booked_by")
		data = {'seat_no':book_pk,'train':pk,'booked_by':booked_by}#,'passanger_name':passanger_name,'aadhar_no':aadhar_no}
		serializer = BookedbySerializer(data=data)
		if serializer.is_valid():
			bookedby = serializer.save() 
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserCreate(generics.CreateAPIView):
	#authentication_classes = ()
	#permission_class =()
	serializer_class = UserSerializer 

class LoginView(APIView):
	permission_classes = ()
	def post(self, request,):
		username = request.data.get("username")
		password = request.data.get("password")
		user = authenticate(username=username, password=password)
		if user:
			return Response({"token": user.auth_token.key})
		else:
			return Response({"error": "worng credentials"}, status=HTTP_400_BAD_REQUEST)

