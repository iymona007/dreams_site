from django.contrib import admin

from .models import Bottle, Mission, MissionCompletion, UserStats

admin.site.register(UserStats)
admin.site.register(Mission)
admin.site.register(MissionCompletion)
admin.site.register(Bottle)
