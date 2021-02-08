from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        values = {
            "username":username,
            "password":password
        }
        return values

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=12,min_length=4,label="Username")
    password=forms.CharField(max_length=18,min_length=6,label="Password",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=18,min_length=6,label="Confirm your password",widget=forms.PasswordInput)
    
    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        confirm=self.cleaned_data.get('confirm')
        if password and confirm and password != confirm:
            raise forms.ValidationError("Password must match")
        values = {
            "username":username,
            "password":password
        }
        return values
