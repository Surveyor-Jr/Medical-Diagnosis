from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .functions import run_diagnosis, search_for_drug


def home(request):
    return render(request, 'home.html')


@login_required
def diagnosis(request):
    """
    diagnosis of the patient based on symptoms
    """
    if request.method == 'POST':
        return run_diagnosis(request)

    else:
        return render(request, 'diagnosis/symptons_form.html', context={
            "result": 'An error occurred Bro'
        })


@login_required
def search_drug(request):
    """
    search for drug and find possible medication & information
    """
    if request.method == 'GET':
        return search_for_drug(request)

    else:
        return render(request, 'diagnosis/search_for_drugs.html', {"drug_name": 'Null'})


# Important Pages
def About(request):
    return render(request, 'static_pages/about.html')


def Pricing(request):
    return render(request, 'static_pages/pricing.html')


def FAQ(request):
    return render(request, 'static_pages/faq.html')


def TermsConditions(request):
    return render(request, 'static_pages/terms_conditions.html')


def PrivacyPolicy(request):
    return render(request, 'static_pages/privacy_policy.html')


def Disclaimer(request):
    return render(request, 'static_pages/disclaimer.html')
