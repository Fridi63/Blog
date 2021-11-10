from django.db import models
from blog.mixins import CreatedModifiedMixin
from account.models import User


class Category(CreatedModifiedMixin):

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Post(CreatedModifiedMixin):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=3000)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.author



class Comment(CreatedModifiedMixin):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user


class Like(CreatedModifiedMixin):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
