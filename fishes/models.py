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
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, related_name="profile")

    class Meta:
        abstract = True

class Student(UserProfile):
    #represents the student object within Goalfish.
    pass

class StudentForm(ModelForm):
    
    class Meta:
        model = Student

class Teacher(UserProfile):
    pass

class TeacherForm(ModelForm):
    
    class Meta:
        model = Teacher

class Mentor(UserProfile):
    pass

class Mentorform(ModelForm):

    class Meta:
        model = Mentor
        
class Sponsor(UserProfile):
    pass

class SponsorForm(ModelForm):

    class Meta:
        model = Sponsor

class Parent(UserProfile):
    pass

class ParentForm(ModelForm):
    
    class Meta:
        model = Parent
        