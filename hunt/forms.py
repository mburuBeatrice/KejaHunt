from django import forms
from .models import House

class NewHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['Location','Image','Description','Type','contact_email','contact_number','category'] 