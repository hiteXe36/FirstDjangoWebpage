from django.shortcuts import render

# dummy data
posts = [
    {
        'author': 'Paul Mathia',
        'title': 'Blog Post1',
        'content': 'first post content',
        'date_posted': 'May 25, 2020'
    },
    {
        'author': 'Gigi',
        'title': 'Blog Post2',
        'content': 'second post content',
        'date_posted': 'May 29, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)


def about(request):
    return render(request, 'blogapp/about.html', {'title': 'About'})
