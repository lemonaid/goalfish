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
from Goalfish.groups.models import Classes, ExtraCurricularActivity

class ClassesAdmin(admin.ModelAdmin):
    save_on_top = True
    
class ExtraCurricularActivityAdmin(admin.ModelAdmin):
    save_on_top = True
    
admin.site.register(Classes, ClassesAdmin)
admin.site.register(ExtraCurricularActivity, ExtraCurricularActivityAdmin)