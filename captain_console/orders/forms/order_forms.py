from django.forms import ModelForm, widgets

from orders.models import BillingDetails, PaymentDetails


class BillingForm(ModelForm):
    class Meta:
        model = BillingDetails
        exclude = ['id']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class PaymentForm(ModelForm):
    class Meta:
        model = PaymentDetails
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expiry_date': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvc_number': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
