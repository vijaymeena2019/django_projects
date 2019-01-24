# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile

# class UserRegisterForm(UserCreationForm):
# 	email = forms.EmailField()  # email = forms.EmailField(requried = false) when email id providing is optional

# 	class Meta:    # This class meta gives us a nested namespace for configuration and keeps th configuration in one place and within the configuration we are saying that the model that will be affected is the user model
# 		model = User # example when we do a form.save() it is going to save it to this user model
# 		fields= ['username', 'email', 'password1', 'password2'] #  the fields that we have here in this list are the fields that we want in the form and in what order

# class UserUpdateForm(forms.ModelForm): # it was similar to above class so copy and edit

# 	email = forms.EmailField()  # email = forms.EmailField(requried = false) when email id providing is optional

# 	class Meta:    
# 		model = User 
# 		fields= ['username', 'email'] 


# class ProfileUpdateForm(forms.ModelForm):
# 	#now we do not want additional fields here so jump 
# 	class Meta:
# 		model = Profile
# 		fields = ['image']


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']