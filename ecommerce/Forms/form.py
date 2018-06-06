from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullName = forms.CharField(
         widget=forms.TextInput(
             attrs={
                 "class": "form-control",
                 "placeholder": "Your Full Name"
             }
         )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Your Message"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be @gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
         widget=forms.TextInput(
             attrs={
                 "class": "form-control",
                 "placeholder": " Username"
             }
         )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"Password"
            }
        )
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
         widget=forms.TextInput(
             attrs={
                 "class": "form-control",
                 "placeholder": " Username"
             }
         )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"Password"
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password"
            }
        )
    )
    def clean_user(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Password must match")
        return data

