from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Anubhav',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Febuary 27, 2020'
    },
    {
        'author': 'Anubhav',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Febuary 28, 2020'
    },
    {
        'author': 'Anubhav',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'Febuary 29, 2020'
    },
]


def home(request):
    # passing posts which is a list[] of dict{} containing multiple posts
    context = {
        'posts': posts
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
