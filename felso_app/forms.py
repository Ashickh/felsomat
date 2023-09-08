from django import forms
from .models import Item, Assembly
from django.forms import ModelForm

class ComponentsForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

        

class GroupsForm(forms.ModelForm):
    class Meta:
        model = Assembly
        fields = "__all__"

        