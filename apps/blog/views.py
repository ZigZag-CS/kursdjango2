from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import Category

# def home(request):
#     if request.method == "POST":
#         return HttpResponse("Hi. this is post request!")
#     elif request.method == "GET":
#         return HttpResponse("Hi. this is get request!")

class HomeView(View):
    """Home page"""
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "blog/home.html", {"categories":category_list})

    def post(self, request):
        return HttpResponse("Hi. this is post request!")

class CategoryView(View):
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, "blog/post_list.html", {"category": category})