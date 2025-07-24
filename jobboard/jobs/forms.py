from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company_name', 'title','description','location','job_type']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume','cover_letter']

class JobSearchForm(forms.Form):
    keyword = forms.CharField(required=False, label='Keyword')
    location = forms.CharField(required=False)
    job_type = forms.ChoiceField(required=False, choices=[('','Any')]+Job.JOB_TYPES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_type'].widget.attrs.update({
            'class': 'form-select custom-select'
        })
