from rest_framework import generics
from .serializers import PropertySerializer,CitySerializer
from .pagination import LargeResultsSetPagination
from sale.models import City,PropertyType,PurchaseType,Property,PropertyFeature,PorpertyImage
from .permissions import IsUpdateaut
class PropertyListAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = LargeResultsSetPagination



class PropertyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsUpdateaut]


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer