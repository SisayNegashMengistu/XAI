from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from .choices import DOCTOR_STATUS

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    status = models.IntegerField(DOCTOR_STATUS, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    doj = models.DateField(null=True)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username

# class Admin_Health_CSV(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     csv_file = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name

class Search_Data(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    prediction_accuracy = models.CharField(max_length=100,null=True,blank=True)
    result = models.CharField(max_length=100,null=True,blank=True)
    values_list = models.CharField(max_length=100,null=True,blank=True)
    created = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.patient.user.username

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    messages = models.TextField(null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.user.username

#my new fetal models
from django.db import models
import os

class Admin_Fetal_Health_CSV(models.Model):
    # FileField to upload CSV files
    csv_file = models.FileField(upload_to='csv_files/', max_length=255)
    # Additional fields if necessary, e.g., name, upload date, etc.
    name = models.CharField(max_length=100, default='ndata.csv', editable=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if self.name else f"CSV File {self.id}"

    def save(self, *args, **kwargs):
        self.csv_file.name = 'ndata.csv'
        super().save(*args, **kwargs)


class FetalDetail(models.Model):
    prolongued_decelerations = models.FloatField()
    percentage_abnormal_long_term_variability = models.FloatField()
    accelerations = models.FloatField()
    abnormal_short_term_variability = models.FloatField()
    severe_decelerations = models.FloatField()
    histogram_variance = models.FloatField()
    light_decelerations = models.FloatField()
    histogram_min = models.FloatField()
    uterine_contractions = models.FloatField()
    mean_value_short_term_variability = models.FloatField()
    histogram_mean = models.FloatField()
    baseline_value = models.FloatField()
    explanation_type = models.CharField(max_length=10, choices=[('lime', 'LIME'), ('shap', 'SHAP')])

    def __str__(self):
        return f"Fetal Detail {self.id}"


class Prediction(models.Model):
    Prolongued = models.FloatField()
    Percentage = models.FloatField()
    Accelerations = models.FloatField()
    Abnormal = models.FloatField()
    Severe = models.FloatField()
    Histogram_variance = models.FloatField()
    light_decelerations = models.FloatField()
    Histogram_min = models.FloatField()
    Uterine_contractions = models.FloatField()
    mean_value = models.FloatField()
    Histogram_mean = models.FloatField()
    Baseline_value = models.FloatField()
    prediction = models.IntegerField()
    accuracy = models.FloatField()
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)