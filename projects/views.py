from django.shortcuts import render
from .models import Projects
# Create your views here.
def home(request):
    project = Projects.objects
    return render(request, 'projects/home.html',{'project':project})