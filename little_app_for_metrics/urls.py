"""
URL configuration for little_app_for_metrics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from rest_framework.routers import SimpleRouter

from library.views import BookViewSet, article_create, article_edit, article_list


router = SimpleRouter()

router.register(r'book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', article_list, name='article-list'),
    path('articles/add/', article_create, name='article-create'),
    path('articles/<int:pk>/edit/', article_edit, name='article-edit'),
]

urlpatterns += router.urls
