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
from Goalfish.fishes.models import Student, Teacher

class Colleges(models.Model):
    
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
    
    name = models.CharField(choices=YEAR_CHOICES, help_text="Your Grade for this School Year")
    notes = models.TextField(null=True,blank=True, help_text="Optional Notes")

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
    
    name = models.CharField(choices=GRADE_CHOICES, help_text="Your Grade")
    notes = models.TextField(blank=True, help_text="Optional Notes")

class ScheduledClass(models.Model):
    
    subject = models.ForeignKey(Subject, help_text="Subject This Class is In")
    teacher = models.ForeignKey(Teacher, help_text="Teacher Offering This Class")
    date_created = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=32)
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def __unicode__(self):
        return "%s-%s" % (str(self.subject), str(self.teacher))
    
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

class Schedule(models.Model):
    
    name = models.CharField(max_length=32, help_text="A Name for This Schedule")
    student = models.ForeignKey(Student)
    classes = models.ManyToManyField(ScheduledClass, help_text="Classes You are Taking This Semester")
    schedule_year = models.ForeignKey(SchoolYear, help_text="Year for This Schedule")
    
    def __unicode__(self):
        return "%s-%s" % (self.name, str(self.schedule_year))
    
class ExtraCurricularActivity(models.Model):
    
    name = models.CharField(max_length=24, unique=True, help_text="Name for this Activity")
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def __unicode__(self):
        return self.name
    
