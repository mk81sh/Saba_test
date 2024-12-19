from django import forms

from product_module.models import Product, ProductColor, Brand, BuiltCountry


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'brand', 'color', 'price', 'display_size', 'built_country', 'is_exist']
        widgets = {
            'price': forms.NumberInput(),
            'display_size': forms.NumberInput(),
            'is_exist': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['brand'].widget.attrs.update({'class': 'form-control'})
        self.fields['color'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['display_size'].widget.attrs.update({'class': 'form-control'})
        self.fields['built_country'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_exist'].widget.attrs.update({'class': 'checkbox'})


class AddProductBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'brand_country', 'url_title', 'is_active']
        widgets = {
            'url_title': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['brand_country'].widget.attrs.update({'class': 'form-control'})
        self.fields['url_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})


class AddProductColorForm(forms.ModelForm):
    class Meta:
        model = ProductColor
        fields = ['name', 'color_code', 'is_active']
        widgets = {
            'is_active': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['color_code'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})


class AddProductBuiltCountryForm(forms.ModelForm):
    class Meta:
        model = BuiltCountry
        fields = ['country', 'url_title', 'is_active']
        widgets = {
            'url_title': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['url_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})
