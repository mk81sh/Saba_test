from django.urls import path

from product_module import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('report', views.ProductFindView.as_view(), name='report'),
    path('brand/<brand>', views.ProductFindView.as_view(), name='brand'),
    path('color/<color>', views.ProductFindView.as_view(), name='color'),
    path('built-country/<bcountry>', views.ProductFindView.as_view(), name='built_country'),
    path('is-exist/<is_exist>', views.ProductFindView.as_view(), name='is_exist'),
    path('is-same/<is_same>', views.ProductFindView.as_view(), name='is_same'),
    path('add-new-product', views.AddNewProductView.as_view(), name='add_new_product'),
    path('add-new-brand', views.AddNewBrandView.as_view(), name='add_new_brand'),
    path('add-new-color', views.AddNewColorView.as_view(), name='add_new_color'),
    path('add-new-built_country', views.AddNewBuiltCountryView.as_view(), name='add_new_built_country'),
]
