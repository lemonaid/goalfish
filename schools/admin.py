from django.contrib import admin
from Goalfish.schools.models import Region, SchoolDistrictSize, SchoolDistrict, SchoolSize, School

class RegionAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'creation_date'
    list_display = ['name', 'creation_date', 'notes_clean']
    ordering = ['name', 'creation_date']


class SchoolDistrictSizeAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True    
    
class SchoolDistrictAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True
    list_display = ['name','creation_date','region','size','primary_contact','get_formatted_address','homepage']
    list_editable = ['name', 'region', 'size', 'primary_contact']
    list_filter = ['region', 'size']
    ordering = ['name','creation_date','region']
    radio_fields = ['region', 'size']
    search_fields = ['name', 'creation_date', 'region', 'size', 'primary_contact', 'notes']
    
class SchoolSizeAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True

class SchoolAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True
    list_display = ['name','mascot','district','creation_date','region','size','primary_contact','get_formatted_address','homepage']
    list_editable = ['name', 'region', 'size', 'primary_contact']
    list_filter = ['region', 'size']
    ordering = ['name','creation_date','region']
    radio_fields = ['region', 'size']
    search_fields = ['name', 'creation_date', 'mascot','district','region', 'size', 'primary_contact', 'notes']
    
admin.site.register(Region, RegionAdmin)
admin.site.register(SchoolDistrictSize, SchoolDistrictSizeAdmin)
admin.site.register(SchoolDistrict, SchoolDistrictAdmin)
admin.site.register(SchoolSize, SchoolSizeAdmin)
admin.site.register(School, SchoolAdmin)