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

from django.db import models
from django.conf import settings
from Goalfish.academics.models import Subject, ClassTime, SchoolTerm
from django.contrib.auth.models import Group

class Classes(Group):

    school_year = models.CharField(max_length=4, editable=False, default=settings.ACTIVE_SCHOOL_YEAR)
    term = models.ForeignKey(SchoolTerm, help_text="Term for this Class")
    class_time = models.ForeignKey(ClassTime, help_text="Time this Class Happens (1st period, 3rd block, etc.)")
    unregistered_teacher = models.CharField(max_length=32, null=True, blank=True, help_text="Please Fill In a Teacher's Name if Your Teacher isn't Registered on Goalfish")
    unregistered_teacher_email = models.EmailField(null=True, blank=True, help_text="If You Know It, that Teacher's Email Address")
    subject = models.ForeignKey(Subject, help_text="Subject of This Class")
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def __unicode__(self):
        return "%s-%s-%s-%s" % (str(self.subject), str(self.class_time), str(self.class_teacher), str(self.school_year))
 
    def has_unregistered_teacher(self):
        if self.unregistered_teacher:
            return True
                
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
    
class ExtraCurricularActivity(Group):
    
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    class Meta:
        verbose_name = "Extra Curricular Activity"
        verbose_name_plural = "Extra Curricular Activities"