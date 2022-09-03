"""harry_potter_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_views = get_schema_view(
    openapi.Info(
        title="Harry Potter API",
        default_version="v1",
        description="A simple API for Harry Potter characters",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="asifazad0178@gmail.com"),   
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/characters/', include('characters.urls')),
    path('api/movies/', include('movies.urls')),
    path('api/spells/', include('spells.urls')),
    path('api/places/', include('places.urls')),

    path('swagger/', schema_views.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_views.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
