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
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic

#
#
# Geographic School Divisions
#
#

class Region(models.Model):
    #represents a collection of school districts
    name = models.CharField(max_length=32, unique=True, help_text="name for this geographic region")
    notes = models.TextField(null=True,blank=True, help_text="optional notes")
    
class SchoolDistrict(models.Model):
    name = models.CharField(max_length=32, unique=True, help_text="name of this school district")
    region = models.ForeignKey(Region, help_text="region this school belongs to")
    notes = models.TextField(null=True,blank=True, help_text="optional notes")
    
class School(models.Model):
    name = models.CharField(max_length=64, unique=True, help_text="name of this school")
    district = models.ForeignKey(SchoolDistrict, help_text="school district this school belongs to")





