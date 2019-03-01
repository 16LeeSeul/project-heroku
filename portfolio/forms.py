from django import forms
from .models import Portfolio

class PortfolioPost(forms.ModelForm): #모델을 기반으로 한 입력 공간, Form: 그냥 공간
    class Meta:
        model = Portfolio # Blog 모델을 기반으로 만듦
        fields = ['title', 'image', 'description'] 
