from django import forms

class AddBoardMemberForm(forms.Form):
	username = forms.CharField(max_length=100)