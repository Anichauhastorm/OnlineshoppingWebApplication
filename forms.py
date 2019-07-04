from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from shop1.models import Profile
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    #name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'NAME'}))
    #dob = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Date of Birth','type':'date'}))
    #phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone no'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
            super(UserCreationForm,self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
            #self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
            self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
            self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirm password'})
class PasswordResetForm:
    class Meta:
        model=User
        fields = ('email')
    def __init__(self,*args,**kwargs):
        super(PasswordResetForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'email'})

#class ProfileForm(forms.ModelForm):
    #class Meta:
       # model = Profile
        #fields = ('name','dob','phone')
