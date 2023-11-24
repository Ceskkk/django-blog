from django import forms
from django.contrib.auth import authenticate
from .models import User


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password'
            }
        )
    )

    password2 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repeat password'
            }
        )
    )

    class Meta:
        model = User
        fields = ("__all__")
        widgets = {
            'email': forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Email",
                }
            ),
            'name': forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Name",
                }
            ),
            'job': forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Job",
                }
            ),
            'birthdate': forms.DateInput(
                attrs={
                    "required": True,
                    "type": "date"
                }
            ),
        }

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):

    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Correo Electronico',
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):

        cleaned_data = super(LoginForm, self).clean()

        email = self.cleaned_data['email']

        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError(
                'Los datos de usuario no son correctos')

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
