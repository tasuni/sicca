from django import forms
from .models import *


class CoinForm(forms.ModelForm):

    class Meta:
        model = Coin
        fields = ['name', 'coin_img']