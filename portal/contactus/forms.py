from django import forms
from .models import contactus

class contactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}))
    # subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'विषय (अनिवार्य)'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = contactus
        # fields = ['title', ]
        # exclude = ['title', ]
        fields = ['name','email','message',]