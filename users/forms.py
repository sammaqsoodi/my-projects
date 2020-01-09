from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import validators
from django.core.validators import RegexValidator

def usernameExist(value):
  if User.objects.filter(username=value).first():
    return True # raise error when user exist


class Register(forms.Form):
  username = forms.CharField(
    label='نام کاربری ',
    max_length=30,
    widget=forms.widgets.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'نام کاربری خود را وارد کنید ',
        'name': 'username',
        'id': 'registerUser',
      }
        ),
    validators=[
      RegexValidator(
        regex= '^[A-Za-z0-9]+(?:[_-][A-Za-z0-9]+)*$',
        message='نام کاربری فرمت نامناسبی دارد.',
        code=30
        )
        ]
    )
  def clean_username(self):
    data = self.cleaned_data.get('username')
    if usernameExist(data):
      raise forms.ValidationError(
      message = 'این نام کاربری قبلا ثبت شده لطفا نام کاربری دیگری انتخاب کنید',
      code = 40
)
    return data

  email = forms.EmailField(
    max_length=200, label='ایمیل ',
      widget=forms.widgets.EmailInput(
            attrs={
                'class': 'form-control',
                'name': 'email',
                'id': 'registerEmail',
                'aria-describedby': "help_email"
            },
        ),
    )

  password1 = forms.CharField(
    label='رمز عبور ',
    max_length=50, min_length=8,
      widget=forms.widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password1',
                'id': 'registerPassword1',
                'aria-describedby': "help_password1"
            }
        ),
    )

  password2 = forms.CharField(
    label='تکرار رمز عبور ',
    max_length=25, min_length=8,
        widget=forms.widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password2',
                'id': 'registerPassword2',
                'aria-describedby': "help_password2"
            }
        ),
    )