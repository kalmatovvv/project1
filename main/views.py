from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import *
from .models import *


class MainPageView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'
    paginate_by = 2

class SearchListView(ListView):
    model = Post
    template_name = 'main/search.html'
    context_object_name = 'results'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        queryset = queryset.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post-info.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = self.get_object().get_image
        context['images'] = self.get_object().images.exclude(id=image)
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'main/create_post.html'
    form_class = CreatePostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        from django.urls import reverse
        return reverse('home')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'main/update_post.html'
    form_class = UpdatePostForm
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        from django.urls import reverse
        return reverse('home')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'main/delete_post.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        from django.urls import reverse
        return reverse('home')

class CategoryListView(ListView):
    model = Post
    template_name = 'main/generic.html'
    context_object_name = 'categories'
# Saved carts

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required
def cart_add(request, id):
    cart = Cart(request)
    post = Post.objects.get(id=id)
    cart.add(product=post)
    return redirect("home")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    post = Post.objects.get(id=id)
    cart.remove(post)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    post = Post.objects.get(id=id)
    cart.add(post=post)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    post = Post.objects.get(id=id)
    cart.decrement(post=post)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url='/account/login/')
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


#Comment

