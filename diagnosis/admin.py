from django.contrib import admin
from .models import *


class DiagnosisResultAdmin(admin.ModelAdmin):
    list_display = ('gender', 'symptom_list', 'diagnosis_name', 'diagnosis_pro_name', 'time_stamp')
    list_filter = ('gender',)
    search_fields = ('diagnosis_result', 'symptom_list')


admin.site.register(Diagnosis_Results, DiagnosisResultAdmin)
