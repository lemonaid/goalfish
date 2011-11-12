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
#from django.forms import ModelForm
from django.contrib.localflavor.us.models import PhoneNumberField, USPostalCodeField, USStateField
from Goalfish.fishes.models import Teacher
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic

class Region(models.Model):
    #represents a collection of school districts
    name = models.CharField(max_length=32, unique=True, help_text="name for this geographic region")
    notes = models.TextField(null=True,blank=True, help_text="optional notes")
    creation_date = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/regions/%s" % self.name
    
    def notes_clean(self):
        return self.notes
    
    notes_clean.allow_tags = True
    
    class Meta:
        verbose_name = "Geographic Region"
    
class SchoolDistrictSize(models.Model):
    min_value = models.IntegerField(max_length=5, help_text="lower range for school district size option")
    max_value = models.IntegerField(max_length=5, help_text="upper range for school district size option")
    
    def __unicode__(self): 
        return "%s - %s" % (str(self.min_value), str(self.max_value)) 
    
class SchoolDistrict(models.Model):
    name = models.CharField(max_length=32, unique=True, help_text="School District Name")
    region = models.ForeignKey(Region, help_text="Geographic Region")
    size = models.ForeignKey(SchoolDistrictSize, help_text="Approximate Size of School District Student Population")
    primary_contact = models.ForeignKey(Teacher, help_text="Primary Contact for this Disctrict")
    primary_phone = PhoneNumberField(help_text="Phone Number")
    address1 = models.CharField(max_length=64, help_text="Address First Line")
    address2 = models.CharField(max_length=64, null=True, blank=True, help_text="Address Second Line (optional)")
    city = models.CharField(max_lenght=32, help_text="City")
    state = USStateField(help_text="US State")
    zip = USPostalCodeField(help_text="ZIP Code")
    homepage = models.URLField(null=True, blank=True, help_text="Website for School District")
    notes = models.TextField(null=True,blank=True, help_text="Optional Notes")
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/school_districts/%s" % self.name
    
    def get_formatted_address(self):
        return "<p>%s<br/>%s<br/>%s<br/>%s %s %s</p>" % (self.name, self.address1, self.address2, self.city, self.state, str(self.zip) )
    
    get_formatted_address.allow_tags = True
    
    class Meta:
        verbose_name = "School District"
        
class SchoolSize(models.Model):
    min_value = models.IntegerField(max_length=5, help_text="lower range for school size option")
    max_value = models.IntegerField(max_length=5, help_text="upper range for school size option")
    
    def __unicode__(self): 
        return "%s - %s" % (str(self.min_value), str(self.max_value)) 
       
class School(models.Model):
    name = models.CharField(max_length=64, unique=True, help_text="School Name")
    district = models.ForeignKey(SchoolDistrict, help_text="School District")
    size = models.ForeignKey(SchoolSize, help_text="Approximate Student Body Size")
    mascot = models.CharField(max_size=32, help_text="School Mascot")
    mascot_logo = models.FileField(upload_to="/mascots/",help_text="Image for Mascot (jpg/png only)")
    primary_contact = models.ForeignKey(Teacher, help_text="Primary Contact for this Disctrict")
    address1 = models.CharField(max_length=64, help_text="Address First Line")
    address2 = models.CharField(max_length=64, null=True, blank=True, help_text="Address Second Line (optional)")
    city = models.CharField(max_lenght=32, help_text="City")
    state = USStateField(help_text="US State")
    zip = USPostalCodeField(help_text="ZIP Code")
    notes = models.TextField(null=True,blank=True, help_text="Optional Notes")
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/schools/%s" % self.name

    def get_formatted_address(self):
        return "<p>%s<br/>%s<br/>%s<br/>%s %s %s</p>" % (self.name, self.address1, self.address2, self.city, self.state, str(self.zip) )
