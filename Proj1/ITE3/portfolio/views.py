from django.shortcuts import render

def index(request):
    return render(request, "pages/portfolio.html")

def contact(request):
    return render(request, "pages/contact.html")

def projects(request):
    return render(request, "pages/projects.html")