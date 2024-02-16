from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.UserListView.as_view(), name='user_list'),
    path('request/', views.RequestView.as_view(), name='request'),
    path('request-list/', views.RequestListView.as_view(), name='request_list'),
    path('accept/', views.AcceptedView.as_view(), name='accepted'),
    path('friends/', views.FriendListView.as_view(), name='friends_list'),
]
