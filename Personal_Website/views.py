from django.shortcuts import render
from Personal_Website.models import Person

# Create your views here.
def home(request):
    return render(request,'index.html')

def Resume(request):
        people = Person.objects.all()
        return render(request,'index.html',{'people':people})

