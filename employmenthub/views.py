from django.shortcuts import render


def index(request):
    context = {
        'title': 'Employment Hub',
    }
    return render(request, 'base.html', context)