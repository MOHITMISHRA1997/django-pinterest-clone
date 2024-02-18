from .models import MyBaseUser,Profile
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User



class UserSignupForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class':'form-control rounded-pill','placeholder':'Username...'}
        )
    )
    email = forms.CharField(
        widget = forms.EmailInput(
            attrs =  {'class':'form-control rounded-pill','placeholder':'Email...'}

        )
    )
    password = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class':'form-control rounded-pill','placeholder':'Password...'}
        )
    )



class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control rounded-pill','placeholder':'Username...'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {'class':'form-control rounded-pill','placeholder':'Password...'}
        )
    )



class UserProfileEditForm(forms.ModelForm):   
    photo = forms.FileField(required=False) 
    class Meta:
        model = Profile
        fields = ("photo","fname","lname","about","pronouns","website")

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm,self).__init__(*args, **kwargs)
        self.fields["photo"].widget.attrs.update({"class": "form-control rounded-pill"})
        self.fields["fname"].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your First Name"})
        self.fields["lname"].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your Last Name"})
        self.fields["about"].widget.attrs.update({"class": "form-control ","placeholder":"Tell something about yourself..."})
        self.fields["pronouns"].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your Pronouns"})
        self.fields["website"].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your website"})


class UserPasswordchangeForm(PasswordChangeForm):   
    class Meta:
        model = User
        fields = ("old_password","new_password1","new_password2")

    def __init__(self, *args, **kwargs):
        super(UserPasswordchangeForm,self).__init__(*args, **kwargs)
        self.fields["old_password"].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your Old password..."})
        self.fields["new_password1"].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your New Password..."})
        self.fields["new_password2"].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Confir your new password..."})

