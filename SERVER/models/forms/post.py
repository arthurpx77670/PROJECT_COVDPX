from django import forms
import datetime


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Titre'}), max_length=100, required=True)
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Détail'}))
    price = forms.FloatField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Mise', 'step': '0.01','id':'price'}), required=True)
    cotation = forms.FloatField(min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Côte','id':'cotation', 'step': '0.1'}), required=True)
    deadline = forms.DateField(widget=forms.SelectDateWidget,initial=datetime.date.today)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False, 'name': 'parcourir'}), required=False)


class CommentaryForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ecriver un commentaire'}), required=True)
    price = forms.FloatField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Mise', 'step': '0.01','classe':'price-com'}), required=True)


class ChatForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'chat-text','placeholder':'Ecriver un message..'}))


class DepositForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), required=True)


class OpinionForm(forms.Form):
    opinion = forms.CharField(widget=forms.Textarea, required=True)
    mark = forms.IntegerField(min_value=0, max_value=20, widget=forms.NumberInput, required=True)


class AutocompleteForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Recherche..',
                                                           'id' : 'myInput',
                                                            'class' : 'form-control',
                                                            "autocomplete" : "off"}), max_length=100, required=True)