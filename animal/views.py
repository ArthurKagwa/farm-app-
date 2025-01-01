from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal
from .serializers import AnimalSerializer

class AnimalList(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)
