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
from Goalfish.academics.models import College, Subject, SchoolYear, Grade, ScheduledClass, SchoolTerm, ExtraCurricularActivity, ClassTime

class CollegeAdmin(admin.ModelAdmin):
    save_on_top = True
    
class SubjectAdmin(admin.ModelAdmin):
    save_on_top = True
    
class SchoolYearAdmin(admin.ModelAdmin):
    save_on_top = True
    
class GradeAdmin(admin.ModelAdmin):
    save_on_top = True
    
class ScheduledClassAdmin(admin.ModelAdmin):
    save_on_top = True
    
class ExtraCurricularActivityAdmin(admin.ModelAdmin):
    save_on_top = True
    
class SchoolTermAdmin(admin.ModelAdmin):
    save_on_top = True
    
class ClassTimeAdmin(admin.ModelAdmin):
    save_on_top = True
    
admin.site.register(College, CollegeAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(ScheduledClass, ScheduledClassAdmin)
admin.site.register(ExtraCurricularActivity, ExtraCurricularActivityAdmin)
admin.site.register(SchoolTerm, SchoolTermAdmin)
admin.site.register(ClassTime, ClassTimeAdmin)