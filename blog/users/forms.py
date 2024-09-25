from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password1'].label = 'Password'
        # self.fields['password2'].label = 'Password Confirmation'
        # self.fields['first_name'].label = 'First Name'
        # self.fields['last_name'].label = 'Last Name'

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']