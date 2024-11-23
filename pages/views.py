from django.shortcuts import render
from posts.models import Post

def index(request):
    posts =  Post.objects.order_by('-post_date').filter(is_published = True)[:6]

    context = {
        'posts':posts
    }

    return render(request, 'pages/index.html' , context  )

def about(request):
    return render(request, 'pages/about.html' )

def m1(request):
    return render(request, 'm6/m1.html')

def m2(request):
    return render(request, 'm6/m2.html')

def m3(request):
    return render(request, 'm6/m3.html')

def m4(request):
    return render(request, 'm6/m4.html')

def m5(request):
    return render(request, 'm6/m5.html')

def m6(request):
    return render(request, 'm6/m6.html')















