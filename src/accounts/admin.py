from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Permission)