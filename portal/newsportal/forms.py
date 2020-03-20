from django import forms
from .models import Category


class Categoryform(forms.ModelForm):
    title=forms.CharField(widget=forms.Textinput(attrs={'class':'form-control','placeholder':'Category Title','title':'Please Enter your title'}))
    description = forms.CharField(widget=forms.Textinput(attrs={'class': 'form-control', 'placeholder': 'Category Description', 'description': 'Describe it'}))
    slug= forms.CharField(widget=forms.Textinput(attrs={'class': 'form-control', 'placeholder': 'Category Slug', 'slug': 'Slug name please'}))


    class Meta:
        model=Category
        fields =['title','description','slug']
        fields= '__all__'


class NewsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'slug'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Category.objects.all())
    status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    rank = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    imageTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    mainNews = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    sliderKey = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    viewCount = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))

    class Meta:
        model = News
        fields ='__all__'