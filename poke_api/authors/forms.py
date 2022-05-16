import re
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User

def add_attr(field,attr_name,attr_new_value):
    existing_attr = field.widget.attrs.get(attr_name,'')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_value}'.strip()

def add_placeholder(field,placeholder_val):
    add_attr(field,'placeholder',placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            'The password must be at least eight characters long, including at least one number or special character, and must not be too common.',
            code='Invalid'
        )

class Register_user(forms.ModelForm):
    def __init__(self,*args, **kwargs ):
        super().__init__(*args, **kwargs)
        add_attr(self.fields['username'],'placeholder','your username')
        add_placeholder(self.fields['email'],'your email')
        add_placeholder(self.fields['first_name'],'ex. : john')
        add_placeholder(self.fields['last_name'],'ex. : doe')

    password_2 = forms.CharField( max_length=15, required=True,widget=forms.PasswordInput(attrs={'placeholder' : 'repeat your password'}),validators=[strong_password] )
    password = forms.CharField( max_length=15, required=True,widget=forms.PasswordInput(attrs={'placeholder' : 'send your password'}))


    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        label='First name'
    )
    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        label='Last name'
    )
    email = forms.EmailField(
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='The e-mail must be valid.',
    )
    class Meta():
        model = User
        fields = ['first_name','last_name','username','email','password']


        widgets = {
            'first_name' : forms.TextInput(attrs={
                'placeholder' : 'type your name here',
            
            }),
            'password' : forms.PasswordInput(attrs={
                'placeholder' : 'type your password here'
            })
        }


    def clean_email(self):
        data = self.cleaned_data.get('email','')
        exists = User.objects.filter(email=data).exists()

        if exists:
            raise ValidationError('User email is already in use',code='Invalid')

        return data




    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')

        if password != password_2 :
            password_confirmation_error = ValidationError('Password is not equal of password_2',code='invalid')
            raise ValidationError({
                'password' : password_confirmation_error,
                'password_2' : [
                    password_confirmation_error,
                    'another error'
                ]
            })