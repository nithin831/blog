from django import forms
from app.models import *

class mail(forms.Form):
	name = forms.CharField()
	mail = forms.EmailField()
	to = forms.EmailField()
	comment = forms.CharField(required=False, widget = forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name',"email", "comment")
    