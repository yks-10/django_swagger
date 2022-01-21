from django.contrib import admin
from django.urls import path, include
from .views import TrainList, TrainDetail, BookList, TrainBook, TrainViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('trains', TrainViewSet, basename='trains')



urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('api-auth/', include('rest_framework.urls')),
    #path('rest-auth/', include('rest_auth.urls')),
    path("trains/", TrainList.as_view(), name="train_list"),
    path("trains/<int:pk>", TrainDetail.as_view(), name="train_detail"),
    path("trains/<int:pk>/books/", BookList.as_view(), name="book_list"),
    path("trains/<int:pk>/books/<int:book_pk>/book/", TrainBook.as_view(), name="booked_by"),
   
    #path("books/", BookList.as_view(), name="book_list"),
    #path("trainbook/", TrainBook.as_view(), name="booked"),
]

urlpatterns+=router.urls