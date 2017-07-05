from django import forms

from .models import SVM_model

class FeatureForm(forms.ModelForm):

    class Meta:
        model = SVM_model 
        fields = ('Haemoglobin', 'WBC', 'Age', 'Smoking', 'Nonveg', 'OccupationType', )