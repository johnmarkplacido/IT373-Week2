from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'features': [
            'Django',
            'Templates',
            'Static Files'
        ]
    }
    return render(request, 'home.html', context)

