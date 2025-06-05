# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):  # UserCreationForm은 기본 유효성 검사 포함
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username' : None,    # 기본 유효성 검사 메시지 제거
            'email' : None,
            'password1' : None,
            'password2' : None,
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'formcontrol'}),
            'email' : forms.EmailInput(attrs={'class' : 'formcontrol'}),
            'password1' : forms.PasswordInput(attrs={'class' : 'formcontrol'}),
            'password2' : forms.PasswordInput(attrs={'class' : 'formcontrol'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['username','email','password1', 'password2']:
            self.fields[field].widget.attrs.update({'class': 'form-control'})