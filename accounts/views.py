from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import LocationsForm, UsersForm, CreateUserForm
from .filters import *
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only


from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
@admin_only
def home(request):
    users = Users.objects.all()
    locations = Locations.objects.all()

    total_users = users.count()
    total_locations = locations.count()

    context = {'users' :users, 'locations' :locations, 'total_users' :total_users, 'total_locations' :total_locations}
    return render(request, 'accounts/dashboard.html', context)



@login_required(login_url='login')
def locations(request):
    locations = Locations.objects.all()
    locationFilter = LocationsFilter(request.GET, queryset=locations)
    locations = locationFilter.qs
    context = {'locations': locations, 'locationFilter': locationFilter}
    return render(request, 'accounts/locations.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def users(request):
    users = Users.objects.all()
    myFilter = UsersFilter(request.GET, queryset=users)
    users = myFilter.qs
    context = {'users' :users, 'myFilter' : myFilter}
    return render(request, 'accounts/users.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createUsers(request):

    form = UsersForm
    if request.method == 'POST':
        #print('Printing Post:', request.POST)
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users')
    context = {'form' :form}
    return render(request, 'accounts/users_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateUsers(request, pk):
    users = Users.objects.get(id=pk)
    form = UsersForm(instance=users)

    if request.method == 'POST':
        #print('Printing Post:', request.POST)
        form = UsersForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect('/users')
    context = {'form' :form}
    return render(request, 'accounts/users_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteUsers(request, pk):
    users = Users.objects.get(id=pk)
    if request.method == "POST":
        users.delete()
        return redirect('/users')
    context = {'item' :users}
    return render(request, 'accounts/deleteusers.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createLocations(request):

    form = LocationsForm

    if request.method == 'POST':
    #return redirect('admin/accounts/locations/add/')

        #form = LocationsForm(request.POST)
        form = LocationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/locations')
    context = {'form' :form}
    return render(request, 'accounts/locations_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateLocations(request, pk):
    locations = Locations.objects.get(id=pk)
    form = LocationsForm(instance=locations)

    if request.method == 'POST':
        #print('Printing Post:', request.POST)
        form = LocationsForm(request.POST, instance=locations)
        if form.is_valid():
            form.save()
            return redirect('/locations')
    context = {'form' :form}
    return render(request, 'accounts/locations_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteLocations(request, pk):
    locations = Locations.objects.get(id=pk)
    if request.method == "POST":
        locations.delete()
        return redirect('/locations')
    context = {'item' :locations}
    return render(request, 'accounts/delete.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='users')
                user.groups.add(group)
                # Added username after video because of error returning customer name if not added


                messages.success(request, 'Account was created for ' + username)
                return redirect('/login')

        context = {'form' :form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')






