from collections.abc import Mapping
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Board
from django import forms



class CreateBoardForm(forms.ModelForm):    
    class Meta:
        model = Board
        fields = ('title','is_private')

    def __init__(self,*args,**kwargs):
        super(CreateBoardForm,self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your board Name"})
        self.fields['is_private'].widget.attrs.update({"class": " form-check-input mt-1 private-checkbox"})



class EditBoardForm(forms.ModelForm):    
    class Meta:
        model = Board
        fields = ('title','cover','is_private','description')

    def __init__(self,*args,**kwargs):
        super(EditBoardForm,self).__init__(*args, **kwargs)
        self.fields['cover'].widget.attrs.update({"class": "form-control rounded-pill"})
        self.fields['title'].widget.attrs.update({"class": "form-control rounded-pill","placeholder":"Your board Title"})
        self.fields['is_private'].widget.attrs.update({"class": " form-check-input mt-1 private-checkbox"})
        self.fields['description'].widget.attrs.update({"class": " form-control "})



