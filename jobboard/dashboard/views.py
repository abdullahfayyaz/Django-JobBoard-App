from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.models import Job, Application

# Create your views here.
class CompanyDashboard(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'dashboard/company.html'
    def get_queryset(self):
        return Job.objects.filter(company=self.request.user)

class ApplicantDashboard(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'dashboard/applicant.html'
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)    