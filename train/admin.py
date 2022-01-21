from django.contrib import admin
from .models import Train, Book, Bookedby

admin.site.register(Train)
admin.site.register(Book)
admin.site.register(Bookedby)

