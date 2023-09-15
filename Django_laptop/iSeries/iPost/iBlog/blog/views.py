from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from .forms import post_form
from django.shortcuts import render

#def home(request):
    #return render(request, 'home.html', {})

class home(ListView):
    model = post
    template_name = 'home.html'
    ordering = ['date_of_creation']

class article(DetailView):
    model = post
    template_name = 'article.html'

class createpost(CreateView):
    model = post
    form_class = post_form
    template_name = 'create_post.html'
    #fields = '__all__'

class updatepost(UpdateView):
    model = post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

class deletepost(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def category(request, id):
    category_posts = post.objects.filter(category=id.replace('-', ' '))
    return render(request, 'categories.html', {'id' : id.title().replace('-', ' '), 'category_posts':category_posts})
