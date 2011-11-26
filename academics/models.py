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

class College(models.Model):
    
    name = models.CharField(max_length=64, unique=True, help_text="Your College Name")
    mascot = models.CharField(max_length=32, help_text="Your College Mascot or Nickname")
    logo = models.ImageField(upload_to="colleges/mascots/", help_text="Optional Logo for Your College")
    website = models.URLField(help_text="Web Site for Your College")
    city = models.CharField(max_length=32, help_text="City of Your College")
    state = USStateField(help_text="State of Your College")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def has_logo(self):
        if self.logo:
            return True
        
    def location(self):
        return "%s, %s" % (self.city, self.state)

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    
    name = models.CharField(max_length=24, help_text="A Classroom Subject")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def admin_notes(self):
        return self.notes
    
    admin_notes.allow_tags = True

    def __unicode__(self):
        return self.name
    
class SchoolYear(models.Model):

    name = models.CharField(max_length=24, help_text="Grade Taught")
    notes = models.TextField(blank=True, help_text="Optional Notes")
 
    def admin_notes(self):
        return self.notes
    
    admin_notes.allow_tags = True
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "School Year"

class SchoolTerm(models.Model):
    
    name = models.CharField(max_length=32, unique=True, help_text="Your School Term (9 weeks, semester, etc.)")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def admin_notes(self):
        return self.notes
    
    admin_notes.allow_tags = True
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "School Term"
    
class ClassTime(models.Model):
    
    name = models.CharField(max_length=32, unique=True, help_text="Time this Class Happens (1st period, 3rd block, etc.)")
    notes = models.TextField(blank=True, help_text="Optional Notes") 

    def admin_notes(self):
        return self.notes
    
    admin_notes.allow_tags = True
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Class Time"

class Grades(models.Model):
    
    GRADE_CHOICES=(
                   ('A','A'),
                   ('B','B'),
                   ('C','C'),
                   ('D','D'),
                   ('E','E'),
                   ('F','F'),
                   )

    name = models.CharField(max_length=1, choices=GRADE_CHOICES)
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def admin_notes(self):
        return self.notes
    
    admin_notes.allow_tags = True

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"