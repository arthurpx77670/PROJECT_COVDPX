from django import forms
from SERVER.models.db.db_profil import Chat


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    text = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}),required=False)


class CommentaryForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class ChatForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'chat-text'}))



