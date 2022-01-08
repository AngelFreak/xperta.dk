# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder':'Navn',
        'class':'form-control',
        }
    ))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder':'Email',
        'class':'form-control',
        }
    ))
    phone = forms.CharField(required=False ,widget=forms.TextInput(
        attrs={'placeholder':'Telefon: valgfri',
        'class':'form-control',
        }
    ))
    company = forms.CharField(required=False ,widget=forms.TextInput(
        attrs={'placeholder':'Firma: valgfri',
        'class':'form-control',
        }
    ))
    subject = forms.CharField(required=True ,widget=forms.TextInput(
        attrs={'placeholder':'Emne',
        'class':'form-control',
        }
    ))
    message = forms.CharField(required=True ,widget=forms.Textarea(attrs={
        'placeholder':'Hvad kan vi hjælpe med ?',
        'class':'form-control',
        }
    ))