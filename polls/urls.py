from django.urls import path
from . import views
# from .views import index
# from .views import (PostListView, 
#     PostDetailView,
#     PostDeleteView, 
#     PostUpdateView,
#     UserPostListView,
#     PostCreateView)

urlpatterns = [
    path('', views.home, name='polls-home'), # path('', views.home, name='blog-home'),
]