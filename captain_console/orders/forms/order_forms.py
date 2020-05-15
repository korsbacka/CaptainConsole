from django.forms import ModelForm, widgets

from orders.models import BillingProfile


class BillingForm(ModelForm):
    class Meta:
        model = BillingProfile
        exclude = ['id', 'user']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'expiry_date': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvc_number': widgets.TextInput(attrs={'class': 'form-control'}),
        }
