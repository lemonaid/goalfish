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
from Goalfish.academics.models import ScheduledClass
from Goalfish.academics.models import Subject, ExtraCurricularActivity, SchoolYear, Grade, College

class Student(User):

    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload")
    favorite_subject = models.ForeignKey(Subject, blank=True, help_text="Your Favorite Subject in School (Optional)")
    extra_curricular_activities = models.ForeignKey(ExtraCurricularActivity, help_text="Other Things Your Do or are Interested In")
    class_year = models.ForeignKey(SchoolYear, help_text="The Year you are going to Graduate High School")
    school = models.ForeignKey(School, help_text="The School You are Currently Attending")
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USStateField(blank=True, help_text="The State You Live In (Optional)")
    zip = USPostalCodeField(blank=True, help_text="Your ZIP Code (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    classes = models.ManyToManyField(ScheduledClass, help_text="Your Classes") 
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")
    
    def __unicode__(self):
        return self.username
    
    def get_absolute_url(self):
        return "/students/%s" % self.id
    
class StudentForm(ModelForm):
    #full form for profile page
    
    class Meta:
        model = Student

class StudentRegisterForm(ModelForm):
    #abbreviated form for new membership
    
    class Meta:
        model = Student
        fields = ('username','first_name','last_name','email','password','favorite_subject','school')
    
class Teacher(User):
    
    SALUTATION_CHOICES=(
                    ('Mr.','Mr.'),
                    ('Mrs.','Mrs.'),
                    ('Ms.','Ms.'),
                    ('Dr.','Dr.'),
                    )

    
    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload")
    salutation = models.CharField(max_length=8, choices=SALUTATION_CHOICES, help_text="Your Preferred Title") 
    subjects_taught = models.ManyToManyField(Subject, help_text="Subject(s) Currently Taught by You")
    sponsorships = models.ManyToManyField(ExtraCurricularActivity, help_text="Any Other Activities you Participate In")
    grades_taught = models.ManyToManyField(Grade, help_text="Grades Currently Teaching")
    school = models.ForeignKey(School, help_text="The School You are Currently Attending")
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USStateField(blank=True, help_text="The State You Live In (Optional)")
    zip = USPostalCodeField(blank=True, help_text="Your ZIP Code (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    website = models.URLField(blank=True, help_text="Your Teacher Website (Optional)")     
    classes = models.ManyToManyField(ScheduledClass, help_text="Your Classes") 
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")

    def __unicode__(self):
        return "%s %s" % (str(self.salutation), self.id)
    
    def get_absolute_url(self):
        return "/teachers/%s" % self.id
    
class TeacherForm(ModelForm):
    
    class Meta:
        model = Teacher

class Sponsor(User):

    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload", verbose_name="Company Logo")
    company_name= models.CharField(max_length=32, unique=True, help_text="Your Company Name")
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USStateField(blank=True, help_text="The State You Live In (Optional)")
    zip = USPostalCodeField(blank=True, help_text="Your ZIP Code (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    website = models.URLField(blank=True, help_text="Your Company Website (Optional)")    
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")

    def __unicode__(self):
        return self.company_name

class SponsorForm(ModelForm):

    class Meta:
        model = Sponsor

class Expertise(models.Model):

    name = models.CharField(max_length=24, unique=True, help_text="Your Expertise")
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def __unicode__(self):
        return self.name

class Mentor(User):
    
    SALUTATION_CHOICES=(
                    ('Mr.','Mr.'),
                    ('Mrs.','Mrs.'),
                    ('Ms.','Ms.'),
                    ('Dr.','Dr.'),
                    )
    
    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload")
    expertise = models.ForeignKey(Expertise, help_text="Your Specialty or Area of Expertise")
    alma_mater = models.ForeignKey(College, blank=True, help_text="College You Attend(ed) - Optional")
    professional_certifications = models.CharField(max_length=32, blank=True, help_text="Any Professional Certifications You Maintain")
    salutation = models.CharField(max_length=8, choices=SALUTATION_CHOICES, help_text="Your Desired Salutation") 
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USStateField(blank=True, help_text="The State You Live In (Optional)")
    zip = USPostalCodeField(blank=True, help_text="Your ZIP Code (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    website = models.URLField(blank=True, help_text="Your Website (Optional)")   
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")


class Mentorform(ModelForm):

    class Meta:
        model = Mentor
        
class Parent(User):

    SALUTATION_CHOICES=(
                    ('Mr.','Mr.'),
                    ('Mrs.','Mrs.'),
                    ('Ms.','Ms.'),
                    ('Dr.','Dr.'),
                    )

    avatar = models.FileField(upload_to="/avatars/", blank=True, help_text="Optional avatar you can upload")    
    salutation = models.CharField(max_length=8, choices=SALUTATION_CHOICES, help_text="Your Desired Salutation") 
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USStateField(blank=True, help_text="The State You Live In (Optional)")
    zip = USPostalCodeField(blank=True, help_text="Your ZIP Code (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    website = models.URLField(blank=True, help_text="Your Website (Optional)")    
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")
    
class ParentForm(ModelForm):
    
    class Meta:
        model = Parent
        