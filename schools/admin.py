'''
This file is part of Goalfish.es.

Goalfish.es is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Goalfish.es is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Goalfish.es.  If not, see <http://www.gnu.org/licenses/>.
'''

from django.contrib import admin
from Goalfish.schools.models import Region, SchoolDistrictSize, SchoolDistrict, SchoolSize, School

class RegionAdmin(admin.ModelAdmin):
    save_on_top = True
    """
    actions_on_bottom = True
    date_hierarchy = 'creation_date'
    list_display = ['name', 'creation_date', 'notes_clean']
    ordering = ['name', 'creation_date']
    """

class SchoolDistrictSizeAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True    
    
class SchoolDistrictAdmin(admin.ModelAdmin):
    save_on_top = True
    """
    actions_on_bottom = True
    list_display = ['name','creation_date','region','size','primary_contact','get_formatted_address','homepage']
    list_editable = ['name', 'region', 'size', 'primary_contact']
    list_filter = ['region', 'size']
    ordering = ['name','creation_date','region']
    #radio_fields = ['region', 'size']
    search_fields = ['name', 'creation_date', 'region', 'size', 'primary_contact', 'notes']
    """
    
class SchoolSizeAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True

class SchoolAdmin(admin.ModelAdmin):
    save_on_top = True
    """
    actions_on_bottom = True
    list_display = ['name','mascot','district','creation_date','region','size','primary_contact','get_formatted_address','homepage']
    list_editable = ['name', 'region', 'size', 'primary_contact']
    list_filter = ['region', 'size']
    ordering = ['name','creation_date','region']
    #radio_fields = ['region', 'size']
    search_fields = ['name', 'creation_date', 'mascot','district','region', 'size', 'primary_contact', 'notes']
    """
admin.site.register(Region, RegionAdmin)
admin.site.register(SchoolDistrictSize, SchoolDistrictSizeAdmin)
admin.site.register(SchoolDistrict, SchoolDistrictAdmin)
admin.site.register(SchoolSize, SchoolSizeAdmin)
admin.site.register(School, SchoolAdmin)