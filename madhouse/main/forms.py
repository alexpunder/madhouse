from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from .models import SignUp
from .validations import spam_validator, username_at_russian_alphabet


class SignUpForm(forms.ModelForm):
    reCAPTCHA = ReCaptchaField(
        label='',
        widget=ReCaptchaV2Checkbox(attrs={
            'data-size': 'normal',
        })
    )
    nickname = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'style': 'display:none;',
        }),
        required=False,
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ваш телефон',
                'type': 'text',
            }
        )
    )

    class Meta:
        model = SignUp
        fields = (
            'name',
            'phone_number',
            'message',
            'nickname',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ваше имя',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ваше сообщение',
                }
            ),
        }

    def save(self, commit=True):
        self.cleaned_data.pop('reCAPTCHA', None)
        return super().save(commit=commit)

    def clean_name(self):
        data = self.cleaned_data.get('name')
        username_at_russian_alphabet(data)
        return data

    def clean_nickname(self):
        data = self.cleaned_data.get('nickname')
        if data:
            raise forms.ValidationError(
                'Введено недопустимое значение, попробуйте другое.'
            )
        return data

    def clean_text(self):
        data = self.cleaned_data.get('text')
        spam_validator(data)
        return data
