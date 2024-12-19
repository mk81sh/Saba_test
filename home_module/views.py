from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home_module/index_page.html')


def header_settings(request):
    return render(request, 'shared/header.html')


def footer_settings(request):
    return render(request, 'shared/footer.html')
