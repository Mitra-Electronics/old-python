# framwork imports
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# project imports
from .forms import UploadForm, CommentForm
import uuid
from .models import Blog, Comment


# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Blog.objects.filter(blog_title__icontains=search)
    return render(request, 'stream_app/home.html', {'videos': blogs, 'search': search, 'result': result})


@login_required
def upload_video(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            title = blog.blog_title
            description = blog.blog_description
            blog.user = request.user
            blog.slug = title.replace(' ', '-') + str(uuid.uuid4())
            blog.save()
            return HttpResponseRedirect(reverse('stream_app:home'))
    return render(request, 'stream_app/upload_video.html', {'form': form})


def details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('stream_app:video_details', kwargs={'slug': slug}))
    return render(request, 'stream_app/video_details.html', {'blog': blog, 'form': comment_form})


@login_required
def edit_video(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = UploadForm(instance=blog)
    if request.method == 'POST':
        form = UploadForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            form = UploadForm(instance=blog)
            return HttpResponseRedirect(reverse('login_app:profile'))

    return render(request, 'stream_app/upload_video.html', {'form': form, 'edit': True})


def services(request):
    return render(request, 'services/services.html', {})