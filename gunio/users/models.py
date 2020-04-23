from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from gunio.common.mixins import TimeStampMixin
from django.http.response import JsonResponse


class User(AbstractUser):

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    profile_image = models.ImageField(upload_to='uploads/', null=True, blank=False)
    address = models.CharField(_("Address"), blank=True, null=False, max_length=255)
    address_cont = models.CharField(_(""), blank=True, null=False, max_length=255)
    address_city = models.CharField(_("City"), blank=True, null=True, max_length=255)
    address_state = models.CharField(_("State"), blank=True, null=False, max_length=255)
    address_zipcode = models.CharField(_("Zipcode"), blank=True, null=False, max_length=255)

    def get_friends(self):
        friends = Friendship.objects.filter(creator=self.id).all()
        return friends

    def get_all_users(self):
        all_users = User.objects.all()
        return all_users

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, related_name="friendship_creator_set", on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friend_set", on_delete=models.CASCADE)
