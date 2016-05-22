from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def files_upload(request):
    return render(request, 'files_upload.html')
