from .models import *
from django import forms

class AddUser_Form(forms.ModelForm):
    class Meta:
        model = UserDataBase
        exclude = ("usr","dob","location","Degree","website", "experience", "company")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", }),
            "email": forms.EmailInput(attrs={"class": "form-control", }),
            "number": forms.NumberInput(attrs={"class": "form-control", }),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),

        }

class Edit_Details(forms.ModelForm):
    class Meta:
        model=UserDataBase
        exclude={"usr"}
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", }),
            "email": forms.EmailInput(attrs={"class": "form-control", }),
            "number": forms.NumberInput(attrs={"class": "form-control", }),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),
            "location": forms.TextInput(attrs={"class": "form-control", }),
            "degree": forms.TextInput(attrs={"class": "form-control", }),
            "website": forms.TextInput(attrs={"class": "form-control", }),
            "experience": forms.TextInput(attrs={"class": "form-control", }),
            "company": forms.TextInput(attrs={"class": "form-control", }),
            "dob": forms.DateInput(attrs={"class": "form-control", }),
        }

class StartCompany_Form(forms.ModelForm):
    class Meta:
        model = Company_Model
        exclude = ("usr",)
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control", }),
            "website":forms.TextInput(attrs={"class":"form-control", }),
            "address":forms.TextInput(attrs={"class":"form-control", }),
            "title":forms.TextInput(attrs={"class":"form-control", }),
            "map_embad":forms.Textarea(attrs={"class":"form-control", }),
            "email":forms.EmailInput(attrs={"class":"form-control", }),
            "number":forms.NumberInput(attrs={"class":"form-control", }),
            "logo":forms.FileInput(attrs={"class":"form-control","onchange":"loadFile(event)" }),

        }

class UserBlog_Form(forms.ModelForm):
    class Meta:
        model = Blogs_Model
        exclude = ("usr",)
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control", }),
            "youtube_video":forms.Textarea(attrs={"class":"form-control", }),
            "blog":forms.Textarea(attrs={"class":"form-control", })

        }