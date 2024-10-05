from django.contrib import admin

# Register your models here.
from .models import CustomUser, Lead, Agent

admin.site.register(CustomUser)
admin.site.register(Lead)
admin.site.register(Agent)