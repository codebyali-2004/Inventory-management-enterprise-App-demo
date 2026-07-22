from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            "product_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Product Name"
            }),
            "category": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Category"
            }),
            "quantity": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Quantity"
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Price"
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }
  