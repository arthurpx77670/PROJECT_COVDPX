from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    text = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}),required=False)


class CommentaryForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


