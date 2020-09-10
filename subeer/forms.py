'''1.Form with opinion
   2.From with ediing new episode in details
   3.Form eding new serial '''

from .models import Opinion
from django import forms


class NameForm(forms.ModelForm):
	
	class Meta:
		model = Opinion
		fields = ['Login', 'Description']

