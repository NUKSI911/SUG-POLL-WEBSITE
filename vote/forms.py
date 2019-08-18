from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from vote.models import Vote, User


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}), label="Matric Number")
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="One of your names"
    )

    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': (
            "Please enter a correct %(username)s and password. "
            "Confirm that your matric number and name combination is correct"
        ),
    }
    


class VotingForm(forms.ModelForm):
    user = forms.CharField(required=False)
    class Meta:
        model = Vote
        fields = '__all__'
        widgets = {'category': forms.HiddenInput(), 'candidate': forms.RadioSelect()}

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    def clean_user(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            raise forms.ValidationError("Admins/Staff cannot vote")
        return self.request.user


class ImportExcelForm(forms.Form):
    file  = forms.FileField(label= "Choose excel to upload")    
