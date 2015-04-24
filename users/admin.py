from django.contrib import admin

# Register your models here.
from .models import *

class ToolAdmin(admin.ModelAdmin):
	class Meta:
		model = Tool

class ShedAdmin(admin.ModelAdmin):
	class Meta:
		model = Shed
		
admin.site.register(Tool, ToolAdmin)
admin.site.register(Shed, ShedAdmin)