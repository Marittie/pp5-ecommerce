from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'blog/',
        views.BlogPostList.as_view(),
        name='blog'
    ),
    path(
        '<int:id>/',
        views.BlogPostDetailView.as_view(),
        name='blog_detail'
    ),
    path(
        'create/',
        views.BlogPostCreateView.as_view(),
        name='create_blog'
    ),
    path(
        'edit/<int:id>/',
        views.EditBlogPostView.as_view(),
        name='edit_blog'
    ),
    path(
        'delete/<int:id>/',
        views.BlogPostDelete.as_view(),
        name='blog_delete'
    ),
]