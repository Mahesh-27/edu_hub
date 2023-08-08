from django import forms
from django.contrib.auth.forms import UserCreationForm

from . models  import *

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=["title","description"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "id": "exampleFormControlInput1",
                "placeholder": "Enter title"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "id": "exampleFormControlTextarea1",
                "rows": 3,
                "placeholder": "Enter description"
            }),
        }

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ["subject", "title", "description", "due", "is_finished"]
        widgets = {
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "id": "exampleFormControlSelect1",
                "placeholder": "Enter Subject"
            }),
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "id": "exampleFormControlInput1",
                "placeholder": "Enter title"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "id": "exampleFormControlTextarea1",
                "rows": 3,
                "placeholder": "Enter description"
            }),
            "due": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "is_finished": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "id": "exampleCheck1",
            }),
        }

class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100,label="Enter Your Search ")
    
    
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["title","is_finished"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "id": "exampleFormControlInput1",
                "placeholder": "Enter title"
            }),
             "is_finished": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "id": "exampleCheck1",
            }),
        }
        
        
class ConversionForm(forms.Form):
    CHOICES=[('length','Length'),('mass','Mass')]
    measurement=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    
class ConversionLengthForm(forms.Form):
    CHOICES=[('yard','Yard'),('foot','Foot')]
    input=forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number'}
    ))
    measure1=forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    measure2=forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    
class ConversionMassForm(forms.Form):
    CHOICES=[('pound','Pound'),('kilogram','Kilogram')]
    input=forms.CharField(required=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number'}
    ))
    measure1=forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    measure2=forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']