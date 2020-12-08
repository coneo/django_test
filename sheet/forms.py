from django import forms

class NameForm(forms.Form):
    data_head = forms.CharField(label='head', max_length=100)
    data_content = forms.CharField(label='content', max_length=1000)
