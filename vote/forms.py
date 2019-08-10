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
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password').lower()

        if username is not None and password:
            try:
                self.user_cache = User.objects.get(matric_number__iexact=username)
                if self.user_cache.first_name.lower() != password and self.user_cache.last_name.lower() != password and self.user_cache.middle_name.lower() != password :
                    raise self.get_invalid_login_error()
                else:
                    self.confirm_login_allowed(self.user_cache)
            except User.DoesNotExist:
                raise self.get_invalid_login_error()
        return self.cleaned_data


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
        return self.request.user


class ImportExcelForm(forms.Form):
    file  = forms.FileField(label= "Choose excel to upload")    