from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title': 'Home'})

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')