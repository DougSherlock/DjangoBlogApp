from django.urls import path
from . import views
# from .views import index
from .views import IndexView 
#     PostDetailView,
#     PostDeleteView, 
#     PostUpdateView,
#     UserPostListView,
#     PostCreateView
#)

app_name = 'polls'


# --- urls that use generic views 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


# --- urls that use 'raw' function views instead of generic views
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'), # path('', views.home, name='blog-home'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]