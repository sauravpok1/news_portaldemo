from django import forms
from .models import Category, News


class CategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'title','placeholder':'Category Title','title':'Please ENter your Title'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'slug','placeholder':'Category slug','title':'Please ENter your Slug'}))
    rank = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Rank','title':'Please ENter your Rank'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
            model = Category
            fields = ['title','slug','rank','description','status' ]
            # fields = '_all_'

class NewsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'slug'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Category.objects.all())
    rank = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    image_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))



    class Meta:
        model = News
        fields =['category','title','slug','rank','image','image_title','description','status','slider_key','main_news',]
        # fields ='__all__'