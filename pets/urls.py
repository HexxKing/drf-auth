from django.urls import path
from .views import PetListCreate, PetRetrieveUpdateDestroy

urlpatterns = [
    path('', PetListCreate.as_view(), name='pet_list_create'),
    path('<int:pk>/', PetRetrieveUpdateDestroy.as_view(), name='pet_retrieve_update_destroy'),
]