from django import forms

class contractform(forms.Form):
    idd = forms.IntegerField()
    firstname = forms.CharField(max_length=120)
    lastname = forms.CharField(max_length=120)
    email = forms.EmailField()

class contractform1(forms.Form):
    roll = forms.IntegerField()
