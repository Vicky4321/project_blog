from django.shortcuts import render
from .models import Blogs
from django.views.generic import ListView

# Create your views here.
class BlogsListView(ListView):
    model = Blogs
    template_name = 'blog/index.html'
    context_object_name = 'profiles'

