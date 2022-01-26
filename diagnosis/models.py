from django.db import models
from django.contrib.auth.models import User


# storage of user query
class Diagnosis_Results(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    symptom_list = models.TextField(null=True)
    diagnosis_name = models.TextField(null=True)
    diagnosis_icd_name = models.TextField(null=True)
    diagnosis_pro_name = models.TextField(null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'Diagnosis Results'


    def __str__(self):
        return str(self.patient)
