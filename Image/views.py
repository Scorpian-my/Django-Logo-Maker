# image_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests

def image_form(request):
    return render(request, 'Image/index.html')


def generate_image(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']

        api_url = f'https://haji-api.ir/ephoto360/?type=text&id={number}&text={name}'
        response = requests.get(api_url)

        if response.status_code == 200:
            return render(request, 'Image/result.html', {'image_url': api_url})
        else:
            return HttpResponse('خطا در دریافت عکس')
    else:
        return HttpResponse('درخواست نامعتبر')

