from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DataConfigForm
from .models import UserDetails
from .userlinks import UserLinks

@login_required
def dashboard(request):
    userlinks = UserLinks(request.user).get_links()
    return render(request, 'dashboard.html', context={'userlinks':userlinks,})

@login_required
def upload(request):
    if request.method == 'POST':
        form = DataConfigForm(request.POST, request.FILES)
        if form.is_valid():
            UserDetails.update_user_files(request.user, request.FILES['datafile'], request.FILES['configfile'])
            return HttpResponseRedirect('/manual_config/')
    else:
        dataconfigform = DataConfigForm()
    return render(request, 'upload.html', {'form': dataconfigform})
 
