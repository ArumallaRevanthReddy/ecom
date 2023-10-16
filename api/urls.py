from django.urls import path
from home.views import getCategories

urlpatterns = [
    path('categories/', getCategories),
]