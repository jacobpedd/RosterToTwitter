from django.contrib import admin
from .models import Roster, Player, TwitterResult, Friend

admin.site.register(Roster)
admin.site.register(Player)
admin.site.register(TwitterResult)
admin.site.register(Friend)