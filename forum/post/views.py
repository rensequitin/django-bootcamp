from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, Author, Comment

def index(request):
    return showAllPosts(request)

def showAllPosts(request):
    template = loader.get_template('post/index.html')
    all_post = Post.objects.all
    all_author = Author.objects.all
    context = { 'all_post' : all_post, 'all_author' : all_author,}
    return HttpResponse(template.render(context, request))

def favorite(request, post_id):

    if 'author_info' not in request.POST:
        return HttpResponseRedirect(reverse('post:index'))

    author_info = request.POST['author_info']
    author = Author.objects.get(pk=author_info)
    post = Post.objects.get(pk=post_id)
    add_comment = post.comment_set.create(comment=request.POST['reply'], author=author)
    add_comment.save()
    return HttpResponseRedirect(reverse('post:index'))

def update(request):
    if 'number' not in request.POST:
        return HttpResponseRedirect(reverse('post:index'))

    comment_id = request.POST['reply-id']
    comment = Comment.objects.get(pk=comment_id)
    comment.comment = request.POST['edit-reply']
    comment.save()
    return HttpResponseRedirect(reverse('post:index'))
