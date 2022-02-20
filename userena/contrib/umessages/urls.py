from django.urls import re_path

from userena.contrib.umessages import views as messages_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    re_path(
        r"^compose/$",
        messages_views.message_compose,
        name="userena_umessages_compose",
    ),
    re_path(
        r"^compose/(?P<recipients>[\+\.\w]+)/$",
        messages_views.message_compose,
        name="userena_umessages_compose_to",
    ),
    re_path(
        r"^reply/(?P<parent_id>[\d]+)/$",
        messages_views.message_compose,
        name="userena_umessages_reply",
    ),
    re_path(
        r"^view/(?P<username>[\.\w]+)/$",
        login_required(messages_views.MessageDetailListView.as_view()),
        name="userena_umessages_detail",
    ),
    re_path(
        r"^remove/$",
        messages_views.message_remove,
        name="userena_umessages_remove",
    ),
    re_path(
        r"^unremove/$",
        messages_views.message_remove,
        {"undo": True},
        name="userena_umessages_unremove",
    ),
    re_path(
        r"^$",
        login_required(messages_views.MessageListView.as_view()),
        name="userena_umessages_list",
    ),
]
