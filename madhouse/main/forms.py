from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
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
