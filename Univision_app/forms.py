from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}), max_length=255)
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}), max_length=254)
