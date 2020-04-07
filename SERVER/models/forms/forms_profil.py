from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    text = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}),required=False)
    price = forms.IntegerField(min_value=0, widget=forms.NumberInput,required=True)
    deadline = forms.DateField(widget=forms.SelectDateWidget)


class CommentaryForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField(min_value=0, widget=forms.NumberInput, required=True)


class ChatForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'chat-text'}))



