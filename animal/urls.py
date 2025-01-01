from django.urls import path
from .views import AnimalList

urlpatterns = [
    path('api/animals/', AnimalList.as_view(), name='animal-list'),
]
