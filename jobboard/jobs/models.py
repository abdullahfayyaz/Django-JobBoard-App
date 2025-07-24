from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):
    JOB_TYPES = [('FT','Full‑Time'),('PT','Part‑Time'),('CT','Contract')]
    company_name = models.CharField(max_length=255, default=None)
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=2, choices=JOB_TYPES)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job','applicant')