from django.contrib import admin
from django.urls import  path, include, re_path
#from rest_framework_swagger.views import get_swagger_view
#drf
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
       title="Train API",
       default_version='v1',
       description="Test description",
       terms_of_service="https://www.ourapp.com/policies/terms/",
       contact=openapi.Contact(email="contact@train.local"),
       license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
 )

#API_TITLE = 'Blog API'
#API_DESCRIPTION = 'A Web API for creating and editing blog posts.'

#schema_view = get_swagger_view(title="TRAIN API")

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include('train.urls')),
   #path('swagger-docs/', schema_view),
   #path('api-auth/', include('rest_framework.urls')),
   #url(r'^rest-auth/registration/',include('rest_auth.registration.urls')),
   #path('api/v1/rest-auth/', include('rest_auth.urls')),
   #path('api/rest_auth/registration/', include('rest_auth.registration.urls')),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
