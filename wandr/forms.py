from django import forms
from django.contrib.auth.models import User
from wandr.models import UserProfile
from wandr.models import Picture

#Cristina:
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

#Cynthia:
class PictureForm(forms.ModelForm):
	name = forms.CharField(max_length=128, required=True, help_text="Name your picture.")
	description = forms.CharField(max_length=200, required=True, help_text="Describe your picture in a short sentence")
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	picture = forms.ImageField(required=True)

	class Meta:
		model = Picture
		fields = ('name', 'description', 'picture')