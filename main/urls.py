from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('categories', CategoryListView.as_view(), name='category'),
    path('<str:slug>/', MainPageView.as_view(), name='list'),

    path('search', SearchListView.as_view(), name='search'),
    path('post-detail/<int:post_id>/', PostDetailView.as_view(), name='detail'),
    path('product/create/', PostCreateView.as_view(), name='create-post'),
    path('product/update/<int:post_id>/', PostUpdateView.as_view(), name='update-post'),
    path('product/delete/<int:post_id>/', PostDeleteView.as_view(), name='delete-post'),


]