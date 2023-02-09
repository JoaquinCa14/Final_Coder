
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from users.forms import RegisterForm, UserUpdateForm, UserProfileForm

from users.models import UserProfile

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context ={
            'form': form
        }
        return render (request, 'users/login.html', context=context)

    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                context = {
                    'message' :f'¡Bienvenido {username}!'
                }
                return render(request, 'index.html', context=context)
        form = AuthenticationForm
        context = {
            'form': form,
            'errors':'Usuario o contraseña incorrecta'
        }
        return render (request, 'users/login.html', context=context)

def register(request):

    if request.method == 'GET':
        form = RegisterForm ()
        context ={
            'form':form
        }
        return render (request, 'users/register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')

        context = {
            'errors': form.errors,
            'form': RegisterForm ()
        }    

        return render(request, 'users/register.html', context=context)

@login_required            
def update_user(request):

    user = request.user
    if request.method == 'GET':
        form = UserUpdateForm(initial = {
                'username':User.username,
                'email':User.email,
                'password':User.password,
                
            }

        )
        context ={
            'form':form
        }
        return render (request, 'users/update.html', context=context)

    elif request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('index')

        context = {
            'errors': form.errors,
            'form': RegisterForm()
        }    

        return render(request, 'users/update.html', context=context)



def update_user_profile(request):

    user = request.user
    if request.method == 'GET':
        form = UserProfileForm (initial={
            'user': request.user.profile.user,
            'phone': request.user.profile.phone,
            'profile_picture': request.user.profile.profile_picture
        })
        context ={
            'form':form
        }
        return render (request, 'users/update_profile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.user = form.cleaned_data.get('user')
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.save()
            return redirect('index')

        context = {
            'errors': form.errors,
            'form': UserProfileForm ()
        }    

        return render(request, 'users/register.html', context=context)