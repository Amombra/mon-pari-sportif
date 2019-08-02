from django.contrib import admin

from  . models import Utilisateur, Match, Choix,Monpars


admin.site.register( Utilisateur)
admin.site.register( Match)
admin.site.register( Choix)
admin.site.register( Monpars)

