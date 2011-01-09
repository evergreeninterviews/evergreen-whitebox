from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationFormWithEmail(UserCreationForm):

    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def get_credentials(self):
        return {
            'username': self.cleaned_data['username'],
            'password': self.cleaned_data['password1']
        }
