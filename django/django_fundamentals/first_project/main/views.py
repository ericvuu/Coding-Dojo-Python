from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def blogs(request):
  return HttpResponse("Blogs")

def index(request):
  return HttpResponse('Placeholder to list all blogs')

def root(request):
  return redirect('/')

def new(request):
  return HttpResponse('New Blog!')

def create(request):
  return redirect('/')

def show(request, num):
  return HttpResponse(f'Blog number {num}')

def edit(request, num):
  return HttpResponse(f"Edit blog number {num}")

def delete(request):
  return redirect('/')

def printjson(request):
  return JsonResponse({"title" : "My first blog", "Content": "Lorem, impsum dolor sit amet consectetur adipiscing elit."})
