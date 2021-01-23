from django.urls import path

from newapi import views
from django.urls import path, include

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]