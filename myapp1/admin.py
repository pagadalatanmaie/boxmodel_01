from django.contrib import admin
from .models import animalwebsite

# Register your models here.
class animalwebsiteAdmin(admin.ModelAdmin):
    list_display=['img','description','author']
admin.site.register(animalwebsite,animalwebsiteAdmin)
