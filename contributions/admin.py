from django.contrib import admin

from .models import Contribution, Topic


admin.site.register(Topic)
admin.site.register(Contribution)
