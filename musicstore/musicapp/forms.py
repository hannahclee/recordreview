from django import forms
from .models import Record, Review, Artist

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields='__all__'

