from django.db import models
from django.contrib.auth.models import AbstractUser


class CreatedModifiedMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, CreatedModifiedMixin):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    # email = models.EmailField(unique=True)
    login = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname


class Profile(CreatedModifiedMixin):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField()
    about_me = models.TextField(max_length=1000)

    def __str__(self):
        return self.user


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


class Subscriber(CreatedModifiedMixin):

    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,  related_name='to_users', on_delete=models.CASCADE)

    def __str__(self):
        return self.to_user # ?


class Comment(CreatedModifiedMixin):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=450)

    def __str__(self):
        return self.user


class Like(CreatedModifiedMixin):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
