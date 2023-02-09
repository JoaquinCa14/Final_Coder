from django import forms

class OrderForms(forms.Form):
    client = forms.CharField(max_length=100)
    product = forms.CharField(max_length=100)
    creation_time = forms.DateTimeField()
    payment_method = forms.BooleanField()