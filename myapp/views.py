from django.http import JsonResponse
import json
from requests import get
from bs4 import BeautifulSoup

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.decorators import login_required
from . models import Match
from . models import Choix
from . models import Utilisateur
from . models import Monpars




def index(request):
    return render(request,'myapp/index.html')

def connexion(request):
    return render(request,'myapp/connexion.html')
"""def parier(request):
    return render(request,'myapp/parier.html')"""

def mylogin(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect('profile')
    else:
        return redirect('login') 

    return redirect('profile')


def inscription(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    try:
        user = User(username = username)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()

        print(username, password)
    except:
        print("Remplir le formulaire")
    return render(request,'myapp/inscription.html')


@login_required(login_url='/login')
def profile(request):
    return render(request,'myapp/profile.html')

def mylogout(request):
    logout(request)
    return redirect('/login')
# Create your views here.

def match(request):
    return render(request,'myapp/match.html')


def affichage(request):
    matchs = Match.objects.all()
    choixs = Choix.objects.all()
    monparss = Monpars.objects.all()
    return render(request,'myapp/affichage.html', {'matchs': matchs, 'choixs':choixs, 'monparss': monparss})

def enregistrer(request):
    if(request.method == 'POST'):
        match1 = Match()

        match1.nomeqA= request.POST['equA']
        match1.nomeqB= request.POST['equB']
        match1.scoreA= request.POST['scA']
        match1.scoreB= request.POST['scB']
        match1.save()
    matchs = Match.objects.all()
    return render(request, 'myapp/match.html', locals())

def monpari(request, id):
    match = Match.objects.get(id = id)
    return render(request, 'myapp/monpari.html', locals())



def monchoix(request):
    if(request.method == 'POST'):
        monpars1 = Monpars()

        monpars1.recup= request.POST['recup']
        monpars1.nom = request.POST['nom']
        monpars1.save()
    monparss = Monpars.objects.all()
    return render(request, 'myapp/affichage.html', locals())

def form(request):
    choixs = Choix.objects.all()
    return render(request,'myapp/form.html', {'choixs': choixs})

def verification(request):
    cote_equA = 1.2
    cote_equB = 1.4
    if(request.method == 'POST'):
        monpars1 = Monpars()

        monpars1.recup= request.POST['recup']
        monpars1.nom = request.POST['nom']
        monpars1.save()
        if( monpars1.recup and cote_equA > cote_equB ):
            return (" 'L'equipe sur laquelle vous avez parié a moins de chance de gagner")
        elif(monpars1.recup and cote_equA < cote_equB):
            return ("Gagné")
    monparss = Monpars.objects.all()

    



















def scrap(request):
    url = 'https://www.matchendirect.fr/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    table = html_soup.find('div', attrs={'id': 'livescore'})
    compt = 1

    mydata = []

    for row in table.findAll('div', attrs={'class': 'panel panel-info'}):

        a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()

        for el in row.findAll('tr'):
            resultat = {}
            heure = el.find('td', attrs={'class': 'lm1'}).get_text()
            eqA = el.find('span', attrs={'class': 'lm3_eq1'}).get_text()
            eqB = el.find('span', attrs={'class': 'lm3_eq2'}).get_text()
            scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

            if el.findAll('td', attrs={'class':'lm2 lm2_1'}):
                resultat['etat'] = el.find('td', attrs={'class':'lm2 lm2_1'})

            resultat['heure'] = heure
            resultat['eqa'] = eqA
            resultat['eqb'] = eqB
            resultat['scors'] = scors
            #resultat['etat'] = etat

            mydata.append(resultat)

    data = mydata

    #return JsonResponse(data, safe=False)  # retourn du json
    return render(request,'myapp/parier.html',{'result':data})

def resultat(request):
    return render(request,'myapp/parier.html')
