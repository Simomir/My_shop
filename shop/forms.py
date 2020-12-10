from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'available')


class ProductUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = "Change Product Image"

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'available')
        widgets = {'image': forms.FileInput()}
