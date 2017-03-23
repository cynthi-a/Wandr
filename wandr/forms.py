from django import forms
from django.contrib.auth.models import User
from wandr.models import UserProfile, Picture

# Registration
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# From to upload Profile Picture
class ProfilePictureForm(forms.ModelForm):
    picture = forms.ImageField(required=False, help_text="Upload your profile photo.")

    class Meta:
        model = UserProfile
        fields = ('picture',)

# Form to upload Cover Photo
class CoverPhotoForm(forms.ModelForm):
    cover_photo = forms.ImageField(required=False, help_text="Upload your Cover photo.")

    class Meta:
        model = UserProfile
        fields = ('cover_photo',)

# Form to upload Pictures
class PictureForm(forms.ModelForm):
    name = forms.CharField(max_length=128, required=True, help_text="Name your picture.")
    description = forms.CharField(max_length=200, required=True, help_text="Describe your picture in a short sentence")
    location = forms.CharField(max_length=128, required=True, help_text="Where did you take this picture?")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    picture = forms.ImageField(required=True)

    class Meta:
        model = Picture
        fields = ('name', 'description', 'picture', 'location')

# contact form might be used in a later version, so it's not deleted
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    form_content = forms.CharField(required=True, widget=forms.Textarea)

# Form for editing profile information
class BioForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea, help_text="Tell the community about yourself.")
    home_town = forms.CharField(required=False, widget=forms.Textarea, help_text="Home town")
    tags = forms.CharField(required=False, widget=forms.Textarea, help_text="")

    class Meta:
        model = UserProfile
        fields = ('bio', 'home_town', 'tags')