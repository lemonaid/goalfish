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
from django.contrib.admin.models import User
from Goalfish.fishes.models import Teacher, Student

class GroupInterest(models.Model):
    name = models.CharField(max_length=24, unique=True, help_text="Interest Name")
    notes = models.TextField(blank=True, help_text="Optional Notes")

class Group(models.Model):
    name = models.CharField(max_length=32, unique=True, help_text="Group Name")
    interest = models.ForeignKey(GroupInterest, help_text="Interest for this Group")
    members = models.ManyToManyField(Student, help_text="Group Members")
    is_public = models.BooleanField(help_text="This Group is Public")
    moderator = models.ForeignKey(User)
                   
class VirtualClassroom(models.Model):
    pass
