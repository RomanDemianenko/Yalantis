"""Yalantis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers

from yala.api.resourse import CourseViewSet
from yala.views import CourseListView, CourseCreateView, CourseUpdateView, CourseDetailView, CourseDeleteView, \
    SearchListView, DateFilterListView

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet, basename="course")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', CourseListView.as_view(), name='course'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='detail'),
    path('create/', CourseCreateView.as_view(), name='create'),
    path('update/<int:pk>', CourseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CourseDeleteView.as_view(), name='delete'),
    path('search_result/', SearchListView.as_view(), name='search'),
    path('filter_date/', DateFilterListView.as_view(), name='date'),
    path('api/', include(router.urls)),
]
