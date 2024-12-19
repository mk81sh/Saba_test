from django import template
from jalali_date import date2jalali

register = template.Library()


@register.filter(name='show_jalali_date')
def show_jalali_date(value):
    months = {
        '1': 'فروردین',
        '2': 'اردیبهشت',
        '3': 'خرداد',
        '4': 'تیر',
        '5': 'مرداد',
        '6': 'شهریور',
        '7': 'مهر',
        '8': 'آبان',
        '9': 'آذر',
        '10': 'دی',
        '11': 'بهمن',
        '12': 'اسفند',

    }
    date = date2jalali(value)
    for month in months:
        if str(date.month) == str(month):
            new_month = months.get(month)
            new_date: str = f'{date.day} {new_month} {date.year}'

    return new_date


@register.filter(name='tdc')
def tdc(value: int):
    return '{:,}'.format(value) + ' تومان'


@register.filter(name='tdc_without_T')
def tdc(value: int):
    return '{:,}'.format(value)
