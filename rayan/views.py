from django.shortcuts import render
from django import forms

from django.http import HttpResponse
from django.urls import reverse

class new_form(forms.Form):
    task=forms.CharField(label='new_task')    

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    if request.method=="POST":
        form=new_form(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            
        else:
            return render(request, 'hello/index2.html', {
                "form":form
            })
    return render(request, 'hello/index.html', {
        'tasks':request.session["tasks"]
    })
    
    
def add(request):

    if request.method=='GET':
        print("Hello")
        return render(request, 'hello/index2.html', {
        "form":new_form()
    })