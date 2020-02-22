from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post # . means in current directory
#from django.http import HttpResponse

# Create your views here.

# posts = [
#     {
#         'author': 'Anubhav',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'Febuary 27, 2020'
#     },
#     {
#         'author': 'Anubhav',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'Febuary 28, 2020'
#     }
# ]


def home(request):
    # passing posts which is a list[] of dict{} containing multiple posts
    # context = {
    #     'posts': posts
    # }
    context = {
        'posts': Post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app><model>_<viewtype>.html
    context_object_name = 'posts'  # same name as context in home function as home.html is expecting 'posts'
    ordering = ['-date_posted']     # default is asc but adding the - before makes it order in desc

class PostDetailView(DetailView):
    # <app>/<model>_<viewtype>.html
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    # <app>/<model>_<viewtype>.html
    # create and update have same page, default naming convention is <app>/<model>_form.html
    # blog/post_form.html
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user    # we are setting the author id here before the form is save by overridding the form_valid function
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):    # the mixins must always be passed first
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user    # we are setting the author id here before the form is save by overridding the form_valid function
        return super().form_valid(form)
    
    # prevent other users from editing another user's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # <app>/<model>_<viewtype>.html
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})


