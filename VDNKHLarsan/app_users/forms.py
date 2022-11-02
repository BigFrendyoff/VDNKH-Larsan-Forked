from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class LoginForm(AuthenticationForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form__input'


class SignUpForm(UserCreationForm):
    patronymic = forms.CharField(widget=forms.TextInput(), required=False)
    born = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'email', 'born')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form__input'


class ProfileForm(forms.ModelForm):
    born = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'patronymic', 'email', 'born')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form__input'


# class ProfileUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form__input'


class WalkRequirementsForm(forms.Form):
    WALKING = (
        ('f', 'быстрая'),
        ('s', 'размеренная'),
        ('i', 'только самое интересное'),
    )
    MONEY = (
        ('f', 'бесплатно'),
        ('p', 'можно платно'),
        ('d', 'без разницы'),
    )
    MOVEMENT = (
        ('f', 'пешком'),
        ('e', 'на электробусах'),
        ('d', 'без разницы'),
    )

    type_of_walking = forms.ChoiceField(choices=WALKING)
    money = forms.ChoiceField(choices=MONEY)
    movement = forms.ChoiceField(choices=MOVEMENT)
