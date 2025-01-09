"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from blog import views  # Make sure views is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('blog/', views.blog_home, name='blog_home'),  # Add this line for blog page
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Post detail page
    path('subscribe/', views.subscribe, name='subscribe'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

