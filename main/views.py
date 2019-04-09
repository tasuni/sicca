from django.shortcuts import render, redirect
import random
from .forms import *

random_number = random.randint(1,5)


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CoinForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/display')
    else:
        form = CoinForm()
    return render(request, 'main/home.html', {'form': form})


def display(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Coins = Coin.objects.all().last()
    return render(request, 'main/display.html', {'coin_image': Coins})