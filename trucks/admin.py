from django.contrib import admin

from .models import Trucks

class TrucksAdmin(admin.ModelAdmin):
    list_display = ('truckgroup', 'shortname', 'longname', 'truckinfo', 'storedplace', 'labelident')
    list_display_links = ('truckgroup', 'shortname', 'longname')
    search_fields = ('truckgroup', 'shortname')


admin.site.register(Trucks, TrucksAdmin)

