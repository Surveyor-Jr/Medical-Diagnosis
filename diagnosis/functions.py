from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Diagnosis_Results
import requests
import json


def run_diagnosis(request) -> object:
    """
    Runs a diagnosis on the patient
    Produces the diagnosis result
    Saves the result to the patients records in the DB
    """
    age = request.POST.get('age')
    female = request.POST.get('female')
    male = request.POST.get('male')  # Not sure if this being used
    symptoms_1 = request.POST.get('symptoms')
    symptoms_2 = request.POST.get('symptoms_1')
    symptoms_3 = request.POST.get('symptoms_2')

    symptoms = [symptoms_1]
    # check for 2nd Symptoms
    if symptoms_2 != 'Select Symptoms':
        symptoms.append(symptoms_2)
    # check for 3rd symptoms
    if symptoms_3 != 'Select Symptoms':
        symptoms.append(symptoms_3)

    for i in range(0, len(symptoms)):
        # convert to integers
        symptoms[i] = int(symptoms[i])

    # check for gender
    if female == 'on':
        sex = 'female'
    else:
        sex = 'male'

    querystring = {
        "gender": sex,
        "year_of_birth": age,
        "symptoms": f"{symptoms}",
        "language": "en-gb"}

    response = requests.request("GET",
                                settings.DIAGNOSIS_URL,
                                headers=settings.DIAGNOSIS_HEADERS,
                                params=querystring
                                )

    diagnosis_result = response.text
    diag_response = json.loads(diagnosis_result)

    name = []
    icd_name = []
    pro_name = []

    for x in range(0, len(diag_response)):
        name.append(diag_response[x]["Issue"]["Name"])
        icd_name.append(diag_response[x]["Issue"]["IcdName"])
        pro_name.append(diag_response[x]["Issue"]["ProfName"])

    diagnosis_list = zip(name, icd_name, pro_name)

    # Save everything to database
    diagnosis_data = Diagnosis_Results(
        patient=request.user,
        gender=sex,
        age=age,
        symptom_list=symptoms,
        diagnosis_name=name,
        diagnosis_icd_name=icd_name,
        diagnosis_pro_name=pro_name
    )
    diagnosis_data.save()

    return render(request, 'diagnosis/symptons_form.html', {"diagnosis": diagnosis_list})

