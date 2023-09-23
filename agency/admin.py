from django.contrib import admin

# Register your models here.
from .models import agency, non_approved_agency


admin.site.register(non_approved_agency)

admin.site.register(agency)