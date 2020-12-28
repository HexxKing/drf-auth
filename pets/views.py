from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pet
from .permissions import IsHumanOrReadOnly
from .serializers import PetSerializer

class PetListCreate(ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (IsHumanOrReadOnly,)
