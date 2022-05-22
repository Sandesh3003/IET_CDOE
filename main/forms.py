from django import forms


class ComingsoonForm(forms.Form):
    email = forms.EmailField(label='',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'id': 'input', 'placeholder': 'Email'}))
