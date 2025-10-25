from django import forms
from .models import ClassificationResultsLog

class LogisticForm(forms.ModelForm):
    class Meta:
        model = ClassificationResultsLog
        fields = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]





