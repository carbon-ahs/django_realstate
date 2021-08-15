from django.shortcuts import render, redirect

def index_view(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'pages_app/index.html', contex)


def about_view(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'pages_app/about.html', contex)