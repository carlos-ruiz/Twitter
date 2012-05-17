from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from main.models import UserProfile, Tweet
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from main.forms import UserCreateForm, LoginForm, EditProfileForm, TweetForm
from django.contrib.auth.models import User
from django.core.context_processors import csrf


def home(request):
    if request.user.is_authenticated():
        return redirect('account')
    else:
        return render_to_response('home.html', {
    }, RequestContext(request))

def Registration(request):
    if request.user.is_authenticated():
            return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
            form = UserCreateForm(request.POST)
            if form.is_valid():
                    user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
                    user.save()
                    users = UserProfile(user=user, name=form.cleaned_data['name'], 
                        birthday=form.cleaned_data['birthday'], location=form.cleaned_data['location'], 
                        bio=form.cleaned_data['bio'], private=form.cleaned_data['private'])
                    users.save()
                    return redirect('LoginRequest')
            else:
                    return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
    else:
            ''' user is not submitting the form, show them a blank registration form '''
            form = UserCreateForm()
            context = {'form': form}
            return render_to_response('register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('profile')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        users = authenticate(username=username, password=password)
                        if users is not None:
                                login(request, users)
                                return redirect('account')
                        else:
                                return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('home.html', context, context_instance=RequestContext(request))

def account(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
    users = request.user.get_profile
    context = {'users': users}
    return render_to_response('account.html', context, context_instance=RequestContext(request))

def profile(request):
    if request.user.is_authenticated():
        users = request.user.get_profile
        usr = UserProfile.objects.get(user=request.user)
        context = {'user': usr, 'users': users}
        return render_to_response('UserProfile.html', context, context_instance=RequestContext(request))
        
    else:
        return HttpResponseRedirect('/login/')


def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/')

def editProfile(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=UserProfile.objects.get(user=request.user))
            if form.is_valid():
                form.save()
                return redirect('profile')
            else:
                return render_to_response('home.html', {'form': form}, RequestContext(request))
        form = EditProfileForm(instance=UserProfile.objects.get(user=request.user))
        dic = {'form': form}
        dic.update(csrf(request))
        return render_to_response('editProfile.html', dic)
    return redirect('login')

def newTweet(request):
    form = TweetForm
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            user = UserProfile.objects.get(user=request.user)
            tweet = Tweet(owner=user, status=form.cleaned_data['status'])
            tweet.save()
            return redirect('account')
    return render_to_response('newTweet.html', {
        'form': form,
        }, RequestContext(request))
