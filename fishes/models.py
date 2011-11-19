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
from django.contrib.localflavor.us.models import PhoneNumberField, USPostalCodeField, USStateField
from Goalfish.schools.models import School

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, related_name="profile")

    class Meta:
        abstract = True

class Student(UserProfile):

    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload")
    favorite_subject = 
    extra_curricular_activities = 
    class_year = 
    school = 
    address1
    address2
    city
    state 
    zip
    twitter
    facebook
    sms
    notes
    
class StudentForm(ModelForm):
    #full form for profile page
    
    class Meta:
        model = Student

class StudentFormNew(ModelForm):
    #abbreviated form for new membership
    
    class Meta:
        model = Student

class Teacher(UserProfile):
    
    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload")
    salutation = 
    subjects_taught = 
    sponsorships = 
    grades_taught = 
    school = 
    address1
    address2
    city
    state 
    zip
    twitter
    facebook
    sms
    website =     
    notes =
     
class TeacherForm(ModelForm):
    
    class Meta:
        model = Teacher

class Sponsor(UserProfile):

    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload", verbose_name="Company Logo")
    company_name=
    address1 = 
    address2 = 
    city = 
    state =
    zip =
    twitter = 
    facebook =
    sms =
    website =     
    notes =

    def __unicode__(self):
        return self.company_name

class SponsorForm(ModelForm):

    class Meta:
        model = Sponsor

class Mentor(UserProfile):
    
    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload")
    expertise = 
    alma_mater = 
    professional_certifications = 
    company = sponsor
    salutation = 
    address1
    address2
    city
    state 
    zip
    twitter
    facebook
    sms
    website =     
    notes =

class Mentorform(ModelForm):

    class Meta:
        model = Mentor
        
class Parent(UserProfile):

    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload")    
    salutation = 
    children = '''FK to Student'''
    address1
    address2
    city
    state 
    zip
    twitter
    facebook
    sms
    website =     
    notes =
    
class ParentForm(ModelForm):
    
    class Meta:
        model = Parent
        