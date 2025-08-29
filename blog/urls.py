app_name = "blog"

from django.urls import path
from .views import PostListView, PostDetailView, PublicationCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PublicationCreateView.as_view(), name="publication_create"),
]