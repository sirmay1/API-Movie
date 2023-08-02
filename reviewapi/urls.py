from django.urls import path, include 
from . import views
from rest_framework import routers 


router = routers.DefaultRouter()
router.register('televisions', views.TVView)

urlpatterns = [
    path('', include(router.urls)),
]

#NOTE: Had issues