from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('element/', CategoryDetailView.as_view(), name='elements'),
    path('category/', InfoDetailView.as_view(), name='category'),
    path('search', SearchListView.as_view(), name='search'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
]