app_name = "blog"

from django.urls import path
from .views import PostListView, PostDetailView, PublicationCreateView , PublicationUpdateView , PublicationDeleteView 
from django.urls import include

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PublicationCreateView.as_view(), name="publication_create"),
    path("post/<int:pk>/edit/", PublicationUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PublicationDeleteView.as_view(), name="post_delete"),
    path("accounts/", include("django.contrib.auth.urls")),
]

