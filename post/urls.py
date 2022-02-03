from django.urls import path
from django.shortcuts import redirect
from post.views import PostsView, new_post, PostDetail

urlpatterns = [

    path("all/", PostsView.as_view(), name="all_posts"),
    path("new/", new_post, name="new_post"),
    path("<slug:slug>/", PostDetail.as_view(), name="single_post")
]