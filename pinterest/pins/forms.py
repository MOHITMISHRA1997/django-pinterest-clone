from .models import Pin
from django import forms
from boards.models import Board

class Create_Pin_form(forms.ModelForm):
    link = forms.CharField(required=False)
    class Meta:
        model = Pin
        fields =['title','board','file','link','description']

    def __init__(self,user,*args,**kwargs):
        super(Create_Pin_form,self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your pin title"})
        self.fields['board'].queryset = Board.objects.filter(user=user)
        self.fields['file'].widget.attrs.update({"class": " form-check"})
        self.fields['link'].widget.attrs.update({"class": " form-control rounded-pill","placeholder":"Give any link"})
        self.fields['board'].widget.attrs.update({"class": " form-control rounded-pill"})
        self.fields['description'].widget.attrs.update({"class": " form-control","placeholder":"Pin description..."})



class Save_to_board(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['board']

    def __init__(self,user,*args,**kwargs):
        super(Save_to_board,self).__init__(*args,**kwargs)
        self.fields['board'].queryset = Board.objects.filter(user = user)
        self.fields['board'].widget.attrs.update({"class":"board-input border form-control"})