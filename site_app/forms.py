from django import forms
from .models import Booking, ContactMessage


class BookingForm(forms.ModelForm):
    """Форма бронирования тура"""
    
    class Meta:
        model = Booking
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'number_of_people', 'travel_date', 'message'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше имя',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите вашу фамилию',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'example@mail.com',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+996 XXX XXX XXX',
                'required': True
            }),
            'number_of_people': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Количество человек',
                'min': 1,
                'required': True
            }),
            'travel_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Дополнительные пожелания (необязательно)',
                'rows': 4
            }),
        }


class ContactForm(forms.ModelForm):
    """Форма обратной связи"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ваше имя',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ваш email',
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Тема сообщения',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Ваше сообщение',
                'rows': 6,
                'required': True
            }),
        }
