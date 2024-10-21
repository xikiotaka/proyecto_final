from django import forms
from .models import Usuario

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'imagen']
        widgets = {
            'password': forms.PasswordInput(),
        }
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'imagen']
