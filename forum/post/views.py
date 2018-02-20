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

def favorite(request, post_id):
    all_post = Post.objects.all
    post = Post.objects.get(pk=post_id)
    add_comment = post.comment_set.create(comment=request.POST['reply'])
    add_comment.save()
    return render(request,'post/index.html', {'all_post':all_post})
