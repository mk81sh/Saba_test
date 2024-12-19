from symtable import Class

from django.db import models


# Create your models here.
class ProductColor(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='رنگ')
    color_code = models.CharField(max_length=30, unique=True, verbose_name='کد رنگ')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام برند')
    brand_country = models.CharField(max_length=20, verbose_name='کشور برند')
    url_title = models.SlugField(unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند محصولات'

    def __str__(self):
        return self.name


class BuiltCountry(models.Model):
    country = models.CharField(max_length=100, unique=True, verbose_name='کشور سازنده')
    url_title = models.SlugField(unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'کشور سازنده'
        verbose_name_plural = 'کشورهای سازنده'

    def __str__(self):
        return self.country


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='مدل گوشی')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='برند محصول')
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, verbose_name='رنگ محصول')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    display_size = models.PositiveIntegerField(verbose_name='سایز صفحه نمایش')
    built_country = models.ForeignKey(BuiltCountry, default='Korea', on_delete=models.CASCADE,
                                      verbose_name='کشور سازنده')
    is_exist = models.BooleanField(verbose_name='موجود / ناموجود')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return f'{self.title} / {self.brand}'
