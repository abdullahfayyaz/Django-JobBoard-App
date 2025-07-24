from django.urls import path
from .views import CompanyDashboard, ApplicantDashboard

app_name = 'dashboard'
urlpatterns = [
    path('company/', CompanyDashboard.as_view(), name='company'),
    path('applicant/', ApplicantDashboard.as_view(), name='applicant'),
]
