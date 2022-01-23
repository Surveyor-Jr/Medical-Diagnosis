from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
import requests
import json


def home(request):
    return render(request, 'home.html')


@login_required
def diagnosis(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        female = request.POST.get('female')
        male = request.POST.get('male')
        symptoms_1 = request.POST.get('symptoms')
        symptoms_2 = request.POST.get('symptoms_1')
        symptoms_3 = request.POST.get('symptoms_2')

        symptoms = []
        symptoms.append(symptoms_1)
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

        context = {
            # Get top diagnosis for now
            # TODO: Find a way to loop through all
            "name": diag_response[0]["Issue"]["Name"],
            "icd_name": diag_response[0]["Issue"]["IcdName"],
            "pro_name": diag_response[0]["Issue"]["ProfName"]
        }
        return render(request, 'diagnosis/symptons_form.html', context)



    else:
        return render(request, 'diagnosis/symptons_form.html', context={
            "result": 'An error occurred Bro'
        })
