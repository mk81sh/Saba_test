from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, View

from product_module.forms import AddProductForm, AddProductBrandForm, AddProductColorForm, AddProductBuiltCountryForm
from product_module.models import Product, Brand, ProductColor, BuiltCountry


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product_module/product_list.html'
    context_object_name = 'products'


class ProductFindView(ListView):
    model = Product
    template_name = 'product_module/find_product.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        brands = Brand.objects.filter(is_active=True).all()
        context['brands'] = brands

        built_country = BuiltCountry.objects.filter(is_active=True).all()
        context['built_country'] = built_country

        colors = ProductColor.objects.filter(is_active=True).all()
        context['colors'] = colors

        return context

    def get_queryset(self):
        query = super(ProductFindView, self).get_queryset()
        query = query.order_by('id').all()
        brand = self.kwargs.get('brand')
        color = self.kwargs.get('color')
        built_country = self.kwargs.get('bcountry')
        is_exist = self.kwargs.get('is_exist')
        is_same = self.kwargs.get('is_same')

        if brand is not None:
            query = query.filter(brand__url_title__iexact=brand).all()

        if color is not None:
            query = query.filter(color__name__iexact=color).all()

        if built_country is not None:
            query = query.filter(built_country__url_title__iexact=built_country).all()

        if is_exist == 'exist':
            query = query.filter(is_exist=True).all()
        elif is_exist == 'not_exist':
            query = query.filter(is_exist=False).all()

        same_country_product = []
        not_same_country_product = []
        for product in query:
            if product.brand.brand_country == product.built_country.country:
                same_country_product.append(product)
            else:
                not_same_country_product.append(product)

        if is_same == 'same':
            query = same_country_product

        elif is_same == 'not_same':
            query = not_same_country_product

        return query


class AddNewProductView(View):
    def get(self, request):
        add_product_form = AddProductForm()
        return render(request, 'product_module/add_product.html', context={
            'add_product_form': add_product_form,
        })

    def post(self, request):
        add_product_form = AddProductForm(request.POST)
        if add_product_form.is_valid():
            add_product_form.save()
            return redirect(reverse('product_list'))
        return render(request, 'product_module/add_product.html', context={
            'add_product_form': add_product_form,
        })


class AddNewBrandView(View):
    def get(self, request):
        add_brand_form = AddProductBrandForm()
        return render(request, 'product_module/add_brand.html', context={
            'add_brand_form': add_brand_form,
        })

    def post(self, request):
        add_brand_form = AddProductBrandForm(request.POST)
        if add_brand_form.is_valid():
            add_brand_form.save()
            return redirect(reverse('add_new_product'))

        return render(request, 'product_module/add_brand.html', context={
            'add_brand_form': add_brand_form,
        })


class AddNewColorView(View):
    def get(self, request):
        add_color_form = AddProductColorForm()
        return render(request, 'product_module/add_color.html', context={
            'add_color_form': add_color_form,
        })

    def post(self, request):
        add_color_form = AddProductColorForm(request.POST)
        if add_color_form.is_valid():
            add_color_form.save()
            return redirect(reverse('add_new_product'))

        return render(request, 'product_module/add_color.html', context={
            'add_color_form': add_color_form,
        })


class AddNewBuiltCountryView(View):
    def get(self, request):
        add_built_country_form = AddProductBuiltCountryForm()
        return render(request, 'product_module/add_built_country.html', context={
            'add_built_country_form': add_built_country_form,
        })

    def post(self, request):
        add_built_country_form = AddProductBuiltCountryForm(request.POST)
        if add_built_country_form.is_valid():
            add_built_country_form.save()
            return redirect(reverse('add_new_product'))

        return render(request, 'product_module/add_built_country.html', context={
            'add_built_country_form': add_built_country_form,
        })
