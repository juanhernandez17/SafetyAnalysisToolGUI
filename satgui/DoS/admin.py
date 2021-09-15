from django.contrib import admin
from .models import System,Component,Component_State,Component_Property,Environmental_Entity,Environmental_State,Environmental_Property, Transition_Rules

# Register your models here.

# used to see hidden fields in admin view
class SystemAdmin(admin.ModelAdmin):
    readonly_fields = ('id','date_posted')


admin.site.register(System,SystemAdmin)
admin.site.register((Component,Component_State,Component_Property,Environmental_Entity,Environmental_State,Environmental_Property,Transition_Rules))