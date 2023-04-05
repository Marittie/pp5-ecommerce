from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm


class BlogPostList(ListView):
    """ A view to return a list of blog posts"""
    model = BlogPost
    queryset = BlogPost.objects.order_by('created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6


class BlogPostDetailView(DetailView):
    """ A view to see the blog post details"""
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    queryset = BlogPost.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)


class BlogPostCreateView(UserPassesTestMixin, CreateView):
    """ A view to create a blog post """

    form_class = BlogPostForm
    template_name = 'blog/create_blog.html'
    success_url = "/blog/blog/"
    model = BlogPost

    def test_func(self):
        """tests the user has the correct email for superuser"""
        return self.request.user.is_superuser

    def form_valid(self, form):
        """ If form is valid return to browse blog posts """

        messages.success(self.request, 'Blog post created successfully')
        return super(BlogPostCreateView, self).form_valid(form)


class EditBlogPostView(UserPassesTestMixin, UpdateView):
    """ A view to edit a blog post """

    Model = BlogPost
    form_class = BlogPostForm
    success_url = "/blog/blog/"
    template_name = "blog/edit_blog.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)

    def test_func(self):
        """tests the user has the correct email for superuser"""
        return self.request.user.is_superuser

    def form_valid(self, form):
        """ If form is valid return to browse blog posts """
        messages.success(self.request, 'Idea created successfully')
        return super().form_valid(form)


class BlogPostDelete(UserPassesTestMixin, DeleteView):
    """ A view to delete a blog post """
    model = BlogPost
    success_url = "/blog/blog/"
    template_name = "blog/blog_delete.html"

    def test_func(self):
        """tests the user has the correct email for superuser"""
        return self.request.user.is_superuser

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)