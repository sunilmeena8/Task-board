
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
	username = forms.CharField(min_length=1, max_length=20)
	email = forms.EmailField()
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise  ValidationError("Email already exists")
		return email
 
	def clean_password1(self):
		password1 = self.cleaned_data['password1']
		if(len(password1)<8):
			raise ValidationError("Password length must be atleast 8 characters.")
		first_isalpha = password1[0].isalpha()
		if all(c.isalpha() == first_isalpha for c in password1):
			raise forms.ValidationError("The new password must contain at least one letter and at least one digit or" \
                                        " punctuation character.")
		return(password1)

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise ValidationError("Password don't match")
		return password2

	def save(self):
		data = self.cleaned_data
		user = User(username=data['username'],email=data['email'])
		user.set_password(raw_password=data['password1'])
		user.save()

