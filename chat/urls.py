
from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name='posts'),
    path("posts/<int:pk>/", views.PostItemView.as_view(), name="post"),
    path("posts/newpost/", views.post_create, name='createpost'),

]
