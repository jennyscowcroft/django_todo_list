# todo_list/todo_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path(
        "",
        views.ListListView.as_view(),
        name="index"
    ),
    path(
        "login/",
        views.UserLoginView.as_view(),
        name="login"
    ),
    path(
        "logout/",
        views.LogoutView.as_view(next_page='login'),
        name="logout"
    ),
    path(
        "register/",
        views.UserRegisterView.as_view(),
        name="register"
    ),
    path(
        "list/<int:list_id>/",
        views.ItemListView.as_view(),
        name="list"
    ),
    # CRUD patterns for ToDoLists
    path(
        "list/add/",
        views.ListCreate.as_view(),
        name="list-add"
    ),
    path(
        "list/<int:pk>/delete/",
        views.ListDelete.as_view(),
        name="list-delete"
    ),
    # CRUD patterns for ToDoItems
    path(
        "list/<int:list_id>/item/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="item-delete",
    ),
]
