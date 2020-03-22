from django import forms

class AddBoardForm(forms.Form):
	title = forms.CharField(label='title',max_length=100)


class AddBoardListForm(forms.Form):
	title = forms.CharField(label='title',max_length=100)

class AddBoardListCardForm(forms.Form):
	title = forms.CharField(label = 'Title',max_length=100)
	due_date = forms.DateField()
	attachment = forms.FileField()

