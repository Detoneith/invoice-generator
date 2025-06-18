from django import forms
from .models import Invoice
from products.models import Product


class InvoiceForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Produits à facturer",
    )

    class Meta:
        model = Invoice
        fields = ["products"]
