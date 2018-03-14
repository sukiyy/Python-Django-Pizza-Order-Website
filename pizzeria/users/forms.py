from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

def validate_pass(password):
    if not any(c.isupper() for c in password):
        raise ValidationError("Password must contain at least one upper case letter,one lower case letter, and one number. Please reset.")
    if not any(c.islower() for c in password):
        raise ValidationError("Password must contain at least one upper case letter,one lower case letter, and one number. Please reset.")
    if not any(c.isdigit() for c in password):
        raise ValidationError("Password must contain at least one upper case letter,one lower case letter, and one number. Please reset.")


class RegistrationForm(UserCreationForm): # Inherit from default Django form
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    address2 = forms.CharField(required=False,help_text='(Optional)')
    town = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zip_code = forms.CharField(required=True)
    password1 = forms.CharField(validators=[validate_pass])

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'address2',
            'town',
            'state',
            'zip_code',
            #'password',
            #'password2',
            )
   
