from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, )
    last_name = forms.CharField(max_length=30, required=True, )
    email = forms.EmailField(max_length=254, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

from .models import DeliveryAddress

class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        fields = ['address', 'city', 'postal_code']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите адрес доставки'}),
            'city': forms.TextInput(attrs={'placeholder': 'Введите город'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Введите почтовый индекс'}),
        }
        labels = {
            'address': 'Адрес',
            'city': 'Город',
            'postal_code': 'Почтовый индекс',
        }
        error_messages = {
            'address': {
                'required': 'Пожалуйста, укажите адрес доставки.',
            },
            'city': {
                'required': 'Пожалуйста, укажите город.',
            },
            'postal_code': {
                'required': 'Пожалуйста, укажите почтовый индекс.',
            },
        }