from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from appFive.forms import UserForm, UserProfileInfoForm


# Create your views here.
def index(request):
    return render(request, 'appFive/index.html')


@login_required
def special(requests):
    return HttpResponse('You are logged in.')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Creates hash of password
            user.save()

            profile = profile_form.save(commit=False)  # Commit set to false so it does not clash with user save
            profile.user = user  # Creates oneToOne relationship with User model

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'appFive/registration.html',  # Match with the template
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use .get because of simplified html, and no form
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)  # Comes from import above
        print(user)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print('Someone tried to login and failed')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('Invalid login credentials supplied')

    else:
        return render(request, 'appFive/login.html', {})
