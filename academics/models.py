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
from django.contrib.localflavor.us.models import USStateField
from django.conf import settings

class College(models.Model):
    
    name = models.CharField(max_length=64, unique=True, help_text="Your College Name")
    mascot = models.CharField(max_length=32, help_text="Your College Mascot or Nickname")
    city = models.CharField(max_length=32, help_text="City of Your College")
    state = USStateField(help_text="State of Your College")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    
    name = models.CharField(max_length=24, help_text="A Classroom Subject")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class SchoolYear(models.Model):
    
    YEAR_CHOICES=(('2011','2011'),
                  ('2012','2012'),
                  ('2013','2013'),
                  ('2014','2014'),
                  ('2015','2015'),
                  ('2016','2016'),
                  ('2017','2017'),
                  ('2018','2018'),
                  ('2019','2019'),
                  ('2020','2020'),)
    
    name = models.CharField(max_length=4, choices=YEAR_CHOICES, help_text="Your Grade for this School Year")
    notes = models.TextField(null=True,blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class SchoolTerm(models.Model):
    
    name = models.CharField(max_length=32, unique=True, help_text="Your School Term (9 weeks, semester, etc.)")
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def __unicode__(self):
        return self.name
    
class ClassTime(models.Model):
    
    name = models.CharField(max_length=32, unique=True, help_text="Time this Class Happens (1st period, 3rd block, etc.)")
    notes = models.TextField(blank=True, help_text="Optional Notes") 
    
    def __unicode__(self):
        return self.name 

class Grade(models.Model):
    
    GRADE_CHOICES=(('5','Fifth Grade'),
                   ('6','Sixth Grade'),
                   ('7','Seventh Grade',),
                   ('8','Eighth Grade'),
                   ('9','Ninth Grade'),
                   ('10','Tenth Grade'),
                   ('11','Eleventh Grade'),
                   ('12','Twelfth Grade'),
                   )
    
    name = models.CharField(max_length=2, choices=GRADE_CHOICES, help_text="Your Grade")
    notes = models.TextField(blank=True, help_text="Optional Notes")

class ScheduledClass(models.Model):

    #TODO -- needs school culled from student
    school_year = models.CharField(max_length=4, editable=False, default=settings.ACTIVE_SCHOOL_YEAR)
    term = models.ForeignKey(SchoolTerm, help_text="Term for this Class")
    class_time = models.ForeignKey(ClassTime, help_text="Time this Class Happens (1st period, 3rd block, etc.)")
    #this won't be a relationship to the actual teacher field, but can be searchable, etc. and the list will be populated in the view as a select box from a queryset.
    #will have to override the default model form for this class.
    class_teacher = models.CharField(max_length=64, help_text="Teacher for This Class")
    subject = models.ForeignKey(Subject, help_text="Subject of This Class")
    date_created = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def __unicode__(self):
        return "%s-%s-%s-%s" % (str(self.subject), str(self.class_time), str(self.class_teacher), str(self.school_year))
    
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
    
class ExtraCurricularActivity(models.Model):
    
    name = models.CharField(max_length=24, unique=True, help_text="Name for this Activity")
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def __unicode__(self):
        return self.name
    
