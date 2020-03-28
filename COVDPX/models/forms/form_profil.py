from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    text = forms.CharField(widget=forms.Textarea)


class CommentaryForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)