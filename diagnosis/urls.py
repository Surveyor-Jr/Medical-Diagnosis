from django.urls import path, include
from diagnosis import views as diagnosis

urlpatterns = [
    path('medi-search/', diagnosis.search_drug, name='search-for-drug'),
]