from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post
def index(request):
    return showAllPosts(request)

def showAllPosts(request):
    template = loader.get_template('post/index.html')
    all_post = Post.objects.all
    context = { 'all_post' : all_post, }
    return HttpResponse(template.render(context, request))
