from django import forms
from products.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = 'title price category tags'.split()
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Введите название товара"
                }),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите цену'
                }),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                })
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=3,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control'
                                   }))
    password = forms.CharField(max_length=100, min_length=2,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control'
                                   }
                               ))