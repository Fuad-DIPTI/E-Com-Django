from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'image_path', 'price', 'description', 'ratings', 'review_comment', 'stock']
