from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
# Registration
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Internal
from .utils.process import get_element_index, get_names_and_emails, get_players
from .utils.draw import game_draw


def index(request):
    '''Main page

    This is the public site
    '''
    template = loader.get_template('index.html')
    return HttpResponse(template.render(dict(), request))


@login_required
def myspace(request):
    '''Space for registered users
    '''
    template = loader.get_template('myspace.html')
    context = {
        'players': 0
    }
    if request.method == 'POST':
        if 'player_form' in request.POST:
            context['players'] = int(request.POST['players'])
            context['player_range'] = range(1, context['players']+1)
        elif 'create_player_form' in request.POST:
            dictionary_keys = request.POST.keys()
            players = get_players(
                request.POST, get_element_index(dictionary_keys))
            get_pairs = game_draw(players)

    return HttpResponse(template.render(context, request))


def logout(request):
    '''Simple logout action
    After the action, you will be redirected to login page
    '''
    auth.logout(request)
    return redirect('index')


def login(request):
    '''Simple login action
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('myspace')
        else:
            messages.info(request, 'username or password incorrect')
            return redirect('login')
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render(dict(), request))


def signup(request):
    '''Registration action
    '''
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup/')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email exists')
                return redirect('signup/')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                return redirect('login/')
        else:
            messages.info(request, 'password not match')
            return redirect('signup/')
        return redirect('amigosecreto/')

    else:
        template = loader.get_template('signup.html')
    return HttpResponse(template.render(dict(), request))


def creategame(request):
    return HttpResponse('You are creating a game')


def game(request, game_id):
    response = 'You are looking for game {}'.format(game_id)
    return HttpResponse(response)
