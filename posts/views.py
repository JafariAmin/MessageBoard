from django.shortcuts import render
from django.views.generic import ListView
from .models import posts

class HomePageView(ListView):
    model = posts
    template_name = 'home.html'
    context_object_name = 'posts_list'


# Create your views here.
