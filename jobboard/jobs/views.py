from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Job, Application
from .forms import JobForm, ApplicationForm, JobSearchForm

class JobListView(ListView):
    model = Job
    paginate_by = 10
    template_name = 'jobs/job_list.html'
    def get_queryset(self):
        qs = super().get_queryset().order_by('-posted_at')
        form = JobSearchForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['keyword']:
                qs = qs.filter(title__icontains=form.cleaned_data['keyword'])
            if form.cleaned_data['location']:
                qs = qs.filter(location__icontains=form.cleaned_data['location'])
            if form.cleaned_data['job_type']:
                qs = qs.filter(job_type=form.cleaned_data['job_type'])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['search_form'] = JobSearchForm(self.request.GET)
        return ctx

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.is_applicant:
            has = Application.objects.filter(job=self.object, applicant=self.request.user).exists()
            ctx['already_applied'] = has
            ctx['app_form'] = ApplicationForm()
        return ctx

def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_applicant:
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.applicant = request.user
            app.save()
        return redirect('jobs:job_detail', pk=pk)
    return redirect('jobs:job_detail', pk=pk)

class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Job 
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('jobs:job_list')
    def form_valid(self, form): 
        form.instance.company = self.request.user; return super().form_valid(form)
    def test_func(self): 
        return self.request.user.is_company

class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('jobs:job_list')
    def test_func(self): 
        return self.get_object().company == self.request.user

class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = '/'
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('jobs:job_list')
    def test_func(self): 
        return self.get_object().company == self.request.user
