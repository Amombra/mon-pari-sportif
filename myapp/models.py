from django.db import models
import math
from django.contrib.auth.models import User
from django.utils import timezone



class Match(models.Model):
	nomeqA = models.CharField(max_length=100)
	nomeqB = models.CharField(max_length=100)
	scoreA = models.CharField(max_length=5)
	scoreB = models.CharField(max_length=5)
    

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    motdepasse = models.CharField(max_length=100)


    def __str__(self):
        return self.nom

    

class Choix(models.Model):
    resultat = models.CharField(max_length=100)
    preference = models.ForeignKey('Match', on_delete=models.CASCADE)
    utilisateur = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.resultat

class Monpars(models.Model):
    recup = models.CharField(max_length = 100)
    nom = models.CharField(max_length = 100)

    def __str__(self):
        return self.recup
