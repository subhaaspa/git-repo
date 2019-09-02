from django.shortcuts import render
from users_apps.models import User,UserProfileInfo
from users_apps.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render (request,"users_apps/index.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username,password)
        user = authenticate(username=username,password=password)

        if user:

            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("No user is active ")

        else:
            print("OOps someone tried to login")
            return HttpResponse("Wrong userid and password ")

    else:
        return render(request,"users_apps/login.html",context= {})



def register(request):

    registered = False

    if (request.method=='POST'):
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            profile.save()
            registered = True

        else :
            print(" OOps Something went wrong ")
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, "users_apps/registration.html",context = {
                            'registered':registered,
                            'user_form':user_form,
                            'profile_form':profile_form
                                                        })
