from django.urls import path
from .views import ListShoesView, ListUsersView, ListUserShoesView, UpdateUserShoesView


app_name = '[shoes]'


urlpatterns = [
    path('users/', ListUsersView.as_view(), name="users-all"),
    path('shoes/', ListShoesView.as_view(), name="shoes-all"),
    path('getusershoes/', ListUserShoesView.as_view(), name="user-shoes-all"),
    path('updateusershoes/', UpdateUserShoesView.as_view(), name='update-user-shoes')
]
