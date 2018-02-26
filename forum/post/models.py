from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post = models.CharField(max_length=600)
    title = models.CharField(max_length=100)

class Comment(models.Model):
    author = models.ForeignKey(Author, models.SET_NULL, blank=True,null=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment = models.CharField(max_length=600)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment
