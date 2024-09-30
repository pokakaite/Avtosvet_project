from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, TextInput
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password1'].attrs = True
        # self.fields['password1'].label = 'Password'
        # self.fields['password2'].label = 'Password Confirmation'
        # self.fields['us'].label = 'First Name'
        # self.fields['last_name'].label = 'Last Name'
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # widgets = {
        #     'username': TextInput(attrs= {
        #         'placeholder': 'Имя пользователя'
        #     }),
        #     'email': TextInput(attrs= {
        #         'placeholder': 'E-mail'
        #     }),
        #     'password1': Input(attrs= {
        #         'placeholder': 'Пароль',
        #         'width': '200px'
        #     }),
        #     'password2': TextInput(attrs= {
        #         'placeholder': 'Повторите пароль'
        #     }),
        # }
