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
from Goalfish.fishes.models import Student, Teacher, Sponsor, Mentor, Parent
from Goalfish.sponsorship.models import SponsoredItem

class StudentAdmin(admin.ModelAdmin):
    save_on_top = True
    
class TeacherAdmin(admin.ModelAdmin):
    save_on_top = True

class SponsoredItemInline(admin.TabularInline):
    model = SponsoredItem
    extra = 5
    
class SponsorAdmin(admin.ModelAdmin):
    save_on_top = True

    inlines = [SponsoredItemInline,]
    
class MentorAdmin(admin.ModelAdmin):
    save_on_top = True
    
class ParentAdmin(admin.ModelAdmin):
    save_on_top = True
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Parent, ParentAdmin)