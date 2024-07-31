from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from .models import FetalDetail
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ('status', 'user', 'dob', 'doj')
class FetalDetailForm(forms.Form):
    prolonged_decelerations = forms.FloatField(required=True)
    percentage_of_time = forms.FloatField(required=True)
    accelerations = forms.FloatField(required=True)
    abnormal_short_term = forms.FloatField(required=True)
    severe_decelerations = forms.FloatField(required=True)
    histogram_variance = forms.FloatField(required=True)
    light_decelerations = forms.FloatField(required=True)
    histogram_min = forms.FloatField(required=True)
    uterine_contractions = forms.FloatField(required=True)
    mean_value_of = forms.FloatField(required=True)
    histogram_mean = forms.FloatField(required=True)
    baseline_value = forms.FloatField(required=True)
    explanation_type = forms.ChoiceField(choices=[('LIME', 'LIME'), ('SHAP', 'SHAP')])
