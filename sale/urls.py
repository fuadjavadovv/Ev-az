from django.urls import path, re_path
from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.home, name='home'),
    path('property-list/', views.property_list, name='property-list'),
    path('property-detail/<int:pk>/<str:slug>/', views.property_detail, name='property-detail'),
    re_path('^file/(?P<file>\w+)\.(?P<extension>\w+)$', views.example)
]