from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            "short_description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "pub_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }