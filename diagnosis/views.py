from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .functions import run_diagnosis


def home(request):
    return render(request, 'home.html')


@login_required
def diagnosis(request):
    if request.method == 'POST':
        return run_diagnosis(request)

    else:
        return render(request, 'diagnosis/symptons_form.html', context={
            "result": 'An error occurred Bro'
        })
