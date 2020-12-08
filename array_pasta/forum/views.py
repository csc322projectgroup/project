from django.shortcuts import render

def home(request):
    return render(request, 'forum/index.html')

def about_us(request):
    return render(request, 'forum/about_us.html')
