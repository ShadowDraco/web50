import random
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import util

class EntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea())

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "search": util.sort_entries(request.GET.get('q', 'default'))
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title, "data": util.get_entry(title) 
    })

def new(request):

    if request.method == "POST":
        form = EntryForm(request.POST)
        print("\n\n")
        print(form)
        if form.is_valid():
            entry = form.cleaned_data
            # If duplicate entry return error
            if util.get_entry(entry["title"].lower()):
                print("\n\n")
                print("duplicate entry submitted")
                return render(request, "encyclopedia/new.html", {
                "title": entry["title"], "content": entry["content"], 
                "error": "Entry already exists, please try something new or Edit the existing Entry"
                })
            # Duplicate entry passes so create new entry
            print("\n\n")   
            print("New entry created")
            util.save_entry(entry["title"], entry["content"])
            return HttpResponseRedirect(f"/{entry["title"]}")

        else: 
            # Form data error
            return render(request, "encyclopedia/new.html", {
                    "title": "error", "content": "", 
                    "error": "Form Data is INVALID, please try removing html and other harmful data"
                })
    # just visiting
    print("\n\n")
    print("viewing create page")
    return render(request, "encyclopedia/new.html", {
        
    })

def edit(request, title):
    if request.method == "POST":
        form = EntryForm(request.POST)
        
        if form.is_valid():
            entry = form.cleaned_data
            util.save_entry(title, entry["content"])
            return HttpResponseRedirect(f"/{title}")
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title, "content": util.get_entry_editable(title)
            })
    return render(request, "encyclopedia/edit.html", {
        "title": title, "content": util.get_entry_editable(title)
    })

def randomEntry(request):
    entries = util.list_entries()
    entry = random.randrange(0, len(entries))
    return HttpResponseRedirect(f"/{entries[entry]}")