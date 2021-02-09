"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view
# from rest_framework.schemas import get_schema_view

schema_view = get_swagger_view(title='API Swagger')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/recipe/', include('recipe.urls')),
    path('', schema_view)
    # path('schema/', get_schema_view(
    #     title="API Test",
    #     description="API Test from Udemy Course",
    #     version="1.0.0"
    # ), name='openapi-schema')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" static() It makes the media URL available in a development server so we
    can test uploading images for our recipes without having to set up a
    separate web server for serving these media files """
