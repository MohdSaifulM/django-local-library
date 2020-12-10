# imports
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
from .serializers import *


# Create your views here.
@login_required
def index(request):
    # books = Book.objects.exclude(available=False)
    books = Book.objects.all()
    branches_unique = []
    for book in books:
        if book.branch not in branches_unique:
            branches_unique.append(book.branch)
    
    

    return render(request, 'index.html', {"books": books, "branches": branches_unique})

# === authentication ===
def register(request):
    # if user is authenticated, go to index
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    # if it is a POST request, fill form with request.POST
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        # if form is valid save and authenticate
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)

            #login using user
            login(request, user)

            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'register.html', {"form": form})

    form = CustomUserCreationForm()

    return render(request, 'register.html', {"form": form})

def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            form = AuthenticationForm(request.POST)
            messages.error(request, "username or password is wrong")
            return render(request, "login.html", {"form": form})

    else:

        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

# === apis ===

@api_view(['GET', 'PUT'])
def api_borrow(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serialize = BookSerializer(instance=book, data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)

    serialize = BookSerializer(book)

    return Response(serialize.data)