from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    placeholder = "This is a placeholder to later display all blogs."
    return HttpResponse(placeholder)

def new(request):
    response = "This is a placeholder to display a new form to create a new blog."
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number ="1"):
    response = "Placeholder for blog number ", number
    return HttpResponse(response)

def edit(request, number ="1"):
    response = "placeholder to edit blog ", number
    return HttpResponse(response)

def destroy(request, number ="1"):
    response = "placeholder to be deleted ", number
    return redirect('/')


