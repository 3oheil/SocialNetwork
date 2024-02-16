from django.urls import path
from . import views

urlpatterns = [
    path('api/post/', views.PostView.as_view(), name='post'),
    path('api/post/<int:post_pk>/', views.PostView.as_view()),
    path('', views.ApiListView.as_view(), name='list_pai'),
    path('api/post/<int:post_pk>/comments', views.CommentView.as_view(), name = 'comment_view'),
    # path('api/post/<int:post_pk>/likes', )
]
