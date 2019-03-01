from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): #모델을 기반으로 한 입력 공간, Form: 그냥 공간
    class Meta:
        model = Blog # Blog 모델을 기반으로 만듦
        fields = ['title', 'body'] 



# class BlogPost(forms.Form): #모델을 기반으로 한 입력 공간, Form: 그냥 공간
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])

    