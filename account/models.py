from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from blog.mixins import CreatedModifiedMixin


# class AppUserManager(models.Manager):
#
#     def create_user(self, username, email, password):
#         if not username:
#             raise ValueError('Invalid name')
#
#         if not email:
#             raise ValueError('Invalid email')
#
#         if not password:
#             raise ValueError('Invalid password')
#
#         user = self.model(username=username, email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()
#
#         return user


class User(AbstractUser, CreatedModifiedMixin):

    # objects = models.Manager()
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(CreatedModifiedMixin):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars/")
    about_me = models.TextField()

    def __str__(self):
        return self.user


class Subscriber(CreatedModifiedMixin):

    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,  related_name='to_users', on_delete=models.CASCADE)

    def __str__(self):
        return self.to_user
