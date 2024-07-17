from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')
    priority = forms.IntegerField(label='priority', min_value=1, max_value=5)

# Create your views here.
def index(request):
    # look inside the session and locate tasks
    if "tasks" not in request.session:
        # if tasks doesn't exist create it.
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {
        "tasks": request.session["tasks"], })

# when this function is called it renders a view from templates folder
def indexNamed(request, name):
    return render(request, 'tasks/index.html', {
        "tasks": tasks, "name": name}) 

def add(request):
    # check if user submitted form
    if request.method == "POST":
        # Add data from the submitted form
        form = NewTaskForm(request.POST)
        # check form validity 
        if form.is_valid():
            # is form valid gives us cleaned_data variable
            task = form.cleaned_data['task']
            # append validated task
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                'form': form
            })

    # if user is GETting page, just render a new form
    return render(request, 'tasks/add.html', {
        'form': NewTaskForm()
    })