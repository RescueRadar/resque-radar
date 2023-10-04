from django.contrib import admin
from .models import Post

# Register your models here.
from .models import agency, non_approved_agency

class non_approved_agencyAdmin(admin.ModelAdmin):
    actions = ['approve_agency']

    def approve_agency(self, request, queryset):
        for i in queryset:
            i.approve()

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content') 

admin.site.register(non_approved_agency, non_approved_agencyAdmin)
admin.site.register(agency)
admin.site.register(Post, PostAdmin)