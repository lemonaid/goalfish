from django.contrib import admin
from Goalfish.schools.models import Region, SchoolDistrictSize, SchoolDistrict, SchoolSize, School

class RegionAdmin(admin.ModelAdmin):
    save_on_top = True

class SchoolDistrictSizeAdmin(admin.ModelAdmin):
    save_on_top = True
    
class SchoolDistrictAdmin(admin.ModelAdmin):
    save_on_top = True

class SchoolSizeAdmin(admin.ModelAdmin):
    save_on_top = True

class SchoolAdmin(admin.ModelAdmin):
    save_on_top = True
    
admin.site.register(Region, RegionAdmin)
admin.site.register(SchoolDistrictSize, SchoolDistrictSizeAdmin)
admin.site.register(SchoolDistrict, SchoolDistrictAdmin)
admin.site.register(SchoolSize, SchoolSizeAdmin)
admin.site.register(School, SchoolAdmin)