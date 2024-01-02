from django.contrib import admin
# Register your models here.

from .models import BotUser, Feedback
# Register your models here.
admin.site.register(BotUser)
admin.site.register(Feedback)