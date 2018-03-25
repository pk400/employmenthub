from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home | Employment Hub',
    }
    return render(request, 'index.html', context)

def employers(request):
    context = {
        'title': 'Employers | Employment Hub',
    }
    return render(request, 'employers.html', context)

def seekers(request):
    context = {
        'title': 'Job Seekers | Employment Hub',
    }
    return render(request, 'seekers.html', context)