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
from django.forms import ModelForm
from Goalfish.schools.models import School
from Goalfish.fishes.models import Student, Teacher

class Subject(models.Model):
    
    name = models.CharField(max_length=24, help_text="A Classroom Subject")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class SchoolYear(models.Model):
    
    YEAR_CHOICES=(('5','Fifth Grade'),
                  ('6','Sixth Grade'),
                  ('7','Seventh Grade'),
                  ('8','Eighth Grade'),
                  ('9','Ninth Grade'),
                  ('10','Tenth Grade'),
                  ('11','Eleventh Grade'),
                  ('12','Twelfth Grade')
                  )
    
    name = models.CharField(choices=YEAR_CHOICES, help_text="Your Grade for this School Year")
    notes = models.TextField(null=True,blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class ScheduledClass(models.Model):
    
    school_year = models.ForeignKey(SchoolYear, help_text="Year for This School Term")
    subject = models.ForeignKey(Subject, help_text="Subject This Class is In")
    teacher = models.ForeignKey(Teacher, help_text="Teacher Offering This Class")
    student = models.ForeignKey(Student)
    date_added = models.DateTimeField(auto_now=True)
    term_class = models.ManyToManyField(Subject, help_text="The Class(es) Taken This Term")
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def __unicode__(self):
        return "%s-%s" % (str(self.subject), str(self.teacher))