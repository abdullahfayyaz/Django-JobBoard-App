from django.urls import path
from .views import (JobListView, JobDetailView, JobCreateView, 
                    JobUpdateView, JobDeleteView, apply_job)

app_name = 'jobs'
urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('add/', JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/apply/', apply_job, name='apply_job'),
    path('<int:pk>/edit/', JobUpdateView.as_view(), name='job_update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]
