from django.shortcuts import render, redirect
from .models import Person_info

def index(request):
    return render(request, 'forms/index.html')

def submit(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        age = request.POST.get('age')
        person = Person_info(first_name=first_name, last_name=last_name, age=age)
        person.save()
        return redirect('result', status='success', person_id=person.id)

    return redirect('result', status='error')

def result(request, status, person_id=None):
    person = None
    if status == 'success' and person_id:
        person = Person_info.objects.get(id=person_id)
    return render(request, 'forms/result.html', {'status': status, 'person': person})

