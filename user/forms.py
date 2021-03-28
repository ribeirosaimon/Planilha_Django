
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from rest_framework.authtoken.models import Token

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = {'first_name','last_name','phone'}
        labels = {'username':'Usuario/Email'}

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        token = Token.objects.create(user=email)
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','phone')
