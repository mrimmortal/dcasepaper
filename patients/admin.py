from django.contrib import admin
from .models import Patient
from .models import Casepaper
# Register your models here.

admin.site.register(Patient)
admin.site.register(Casepaper)