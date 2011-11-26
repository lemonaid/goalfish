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
from Goalfish.goals.models import TeacherAcademicGoal, AutoGoal, SMARTGoal
    
class TeacherAcademicGoalAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True
    list_display = ('name','goal','reward','is_active')
    search_fields = ('name','goal','reward')
    
class AutoGoalAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True
    list_display = ('name','reward','is_active')
    search_fields = ('name', 'reward')

class SMARTGoalAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom = True
    list_display = ('name', 'begin_date', 'end_date', 'reward','is_active')
    date_heirarchy = 'begin_date','end_date' 
    search_fields = ('name', 'begin_date', 'end_date', 'reward')   
    
admin.site.register(TeacherAcademicGoal, TeacherAcademicGoalAdmin)
admin.site.register(AutoGoal, AutoGoalAdmin)
admin.site.register(SMARTGoal, SMARTGoalAdmin)