from django.contrib import admin
from Goalfish.mentorship.models import Expertise

class ExpertiseAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_bottom= True
    list_display = ('name','admin_notes')
    
admin.site.register(Expertise, ExpertiseAdmin)