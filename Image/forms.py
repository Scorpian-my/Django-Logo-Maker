from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class ImageForm(forms.Form):
    name = forms.CharField(label='نام', max_length=100, required=True)
    number = forms.IntegerField(
        label='عدد',
        required=True,
        validators=[
            MinValueValidator(1, message='عدد وارد شده باید بزرگتر یا مساوی ۱ باشد.'),
            MaxValueValidator(136, message='عدد وارد شده باید کمتر یا مساوی ۱۳۶ باشد.')
        ]
    )
