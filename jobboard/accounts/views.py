from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_applicant = not user.is_company
            user.save()
            login(request, user)
            return redirect('jobs:job_list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})