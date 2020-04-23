from django.urls import path

from gunio.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    delete_view,
    FriendshipCreateView,
    ApproveFreindshipView,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('delete-entry/<pk>/', view=delete_view, name='delete_view'),
    path('add_view/<friend_id>/', view=FriendshipCreateView, name='add_view'),
    path('approve_view/<int:id>/', view=ApproveFreindshipView, name='approve_view'),
]
