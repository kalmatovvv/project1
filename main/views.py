from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import *


class MainPageView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'

class InfoDetailView(ListView):
    model = Post
    template_name = 'main/generic.html'
    context_object_name = 'post'

class CategoryDetailView(ListView):
    model = Category
    template_name = 'main/post-detail.html'
    context_object_name = 'categories'

class SearchListView(ListView):
    model = Post
    template_name = 'main/search.html'
    context_object_name = 'results'

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post-info.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = self.get_object().get_image
        context['images'] = self.get_object().images.exclude(id=image)
        return context