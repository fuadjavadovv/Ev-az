from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog-list/', views.blog_list, name='blog-list'),
    path('blog-detail/', views.blog_detail, name='blog-detail')
]
