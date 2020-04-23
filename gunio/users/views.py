from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, DeleteView, CreateView
from .models import Friendship
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from datetime import datetime

User = get_user_model()


def FriendshipCreateView(request, friend_id):
    friendship = Friendship(creator_id=request.user.id, friend_id=friend_id, status="pending")
    friendship.save()

    return HttpResponseRedirect('/users/'+request.user.username)


def ApproveFreindshipView(request, id):
    friendship = Friendship.objects.get(id=id)
    friendship.status = "approved"
    friendship.approved = datetime.now()
    friendship.save()

    return HttpResponseRedirect('/users/'+request.user.username)


class DeleteView(SuccessMessageMixin, DeleteView):
    model = Friendship
    success_url = '/users/~redirect/'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(DeleteView, self).delete(request, *args, **kwargs)


delete_view = DeleteView.as_view()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["first_name", "last_name", "email", "profile_image"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
