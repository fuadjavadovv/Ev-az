
from django.urls import path, include
from api import views as api_views

urlpatterns = [
    path('property/',api_views.PropertyListAPIView.as_view(), name = 'property' ),
    path('property/<int:pk>',api_views.PropertyDetailAPIView.as_view(), name = 'property-details' ),
    path('city/',api_views.CityListAPIView.as_view(), name = 'city' ),
  


] 