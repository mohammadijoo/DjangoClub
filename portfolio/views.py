from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail
from theblog.models import Post, Profile, Category
from theblogfa.models import Postfa, Categoryfa
from itertools import chain
# Import Pagination
from django.core.paginator import Paginator
import csv
import os
from django.conf import settings
from pathlib import Path
from django.core.files import File


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
    

def en(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/en.html', {'projects': projects})
    
    

def contact(request):
    if request.method == "POST":
        message_fname = request.POST['name']
        message_lname = request.POST['surname']
        message_number = request.POST['phone']
        message_email = request.POST['email']
        message = request.POST['message']

        # Sending EMAIL
        send_mail(
        "Email from: " + message_fname + " " + message_lname , #Subject
        "Email from: " + message_fname + " " + message_lname +
        "\n" + "Email Address: " + message_email + "\n" +
        "Contact Number: " + message_number + "\n" + message,  #Message
        message_email, #from Email
        ['info@django3.ir'], # To Email
        )
        return render(request, 'portfolio/contact.html',{'message_fname': message_fname})
    else:
        return render(request, 'portfolio/contact.html', {})
        
        
        
        
def contactEn(request):
    if request.method == "POST":
        message_fname = request.POST['name']
        message_lname = request.POST['surname']
        message_number = request.POST['phone']
        message_email = request.POST['email']
        message = request.POST['message']

        # Sending EMAIL
        send_mail(
        "Email from: " + message_fname + " " + message_lname , #Subject
        "Email from: " + message_fname + " " + message_lname +
        "\n" + "Email Address: " + message_email + "\n" +
        "Contact Number: " + message_number + "\n" + message,  #Message
        message_email, #from Email
        ['info@django3.ir'], # To Email
        )
        return render(request, 'portfolio/contactEn.html',{'message_fname': message_fname})
    else:
        return render(request, 'portfolio/contactEn.html', {})        
        
        
        
        
def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        SearchResults1 = Post.objects.filter(body__contains=searched)
        SearchResults2 = Profile.objects.filter(bio__contains=searched)
        #SearchResults3 = Post.objects.filter(category__contains=searched)
        #SearchResults4 = Post.objects.filter(title__contains=searched)
        #SearchResults5 = Profile.objects.filter(user__contains=searched)
        #SearchResults6 = Category.objects.filter(name__contains=searched)
        #SearchResults = list(chain(SearchResults1, SearchResults2, SearchResults3, SearchResults4))

        return render(request, 'portfolio/search_results.html', {'searched': searched, 'SearchResults1': SearchResults1, 'SearchResults2': SearchResults2})
    else:
        return render(request, 'portfolio/search_results.html', {})
        
        
        
        
        
        
def search_resultsfa(request):
    if request.method == "POST":
        searchedfa = request.POST['searchedfa']
        SearchResults1 = Postfa.objects.filter(body__contains=searchedfa)
        SearchResults2 = Profile.objects.filter(bio__contains=searchedfa)
        #SearchResults3 = Postfa.objects.filter(title__contains=searchedfa)
        #SearchResults5 = Profile.objects.filter(user__contains=searchedfa)
        #SearchResults6 = Category.objects.filter(name__contains=searchedfa)
        #SearchResults = list(chain(SearchResults1, SearchResults2, SearchResults3, SearchResults4))

        return render(request, 'portfolio/search_resultsfa.html', {'searchedfa': searchedfa, 'SearchResults1': SearchResults1, 'SearchResults2': SearchResults2})
    else:
        return render(request, 'portfolio/search_resultsfa.html', {})
    
    

# BASE_DIR = Path(__file__).resolve().parent.parent
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# file_path = os.path.join(STATIC_ROOT, 'iris.csv')        

# file_path = os.path.join(settings.STATIC_ROOT, 'iris.csv')

# def irisDataset(request):
#     csv_fp = open(file_path, 'r')
#     reader = csv.DictReader(csv_fp)
#     headers = [col for col in reader.fieldnames]
#     out = [row for row in reader]
#     return render(request, 'iris.html', {'data' : out, 'headers' : headers})        
        
        
        
# def custom_404(request, exception):
#     return render(request, 'portfolio/PageNotFound.html')
    
    
def error_404_view(request, exception):
    return render(request, 'PageNotFound.html', status=404)
        
        
        
        
        
        
        
        
        
        
        
        
        
