from django.shortcuts import render
import random

random_number = random.randint(1,5)


# Create your views here.
def home(request):
    context = {
        'content': random_number
    }
    return render(request, 'main/home.html', context)