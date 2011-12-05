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
from django.contrib.auth.models import User, UserManager
from django.forms import ModelForm
from django.contrib.localflavor.us.models import PhoneNumberField, USPostalCodeField
from Goalfish.schools.models import School
from Goalfish.academics.models import Subject, College, SchoolYear
import re

class Student(User):
    '''
    The Student model represents all information tracked by Goalfish for a registered student. 
    '''
    
    avatar = models.FileField(upload_to="avatars/students/", blank=True, help_text="Optional avatar you can upload")
    favorite_subject = models.ForeignKey(Subject, blank=True, help_text="Your Favorite Subject in School (Optional)")
    class_year = models.ForeignKey(SchoolYear, help_text="The Year you are going to Graduate High School")
    school = models.ForeignKey(School, help_text="The School You are Currently Attending")
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USPostalCodeField(blank=True, help_text="The State You Live In (Optional)")
    zip = models.CharField(max_length=10, blank=True, help_text="Your ZIP Code in XXXXX or XXXXX-XXXX Format (Optional)")
    twitter = models.CharField(max_length=64, blank=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")
    
    def __unicode__(self):
        return self.username
    
    def is_student(self):
        """returns True because this is a Student object"""
        return True
    
    def formatted_mailing(self):
        """Provides a properly formatted mailing address"""
        
        return "%s\n%s\n%s\n%s,%s %s" % (self.get_full_name(), self.address1, self.address2, self.city, self.state, self.zip)

    def has_valid_mailing(self):
        """returns True if the student has all of the needed components for a valid mailing address"""
        if self.address1:
            if self.city:
                if self.state:
                    if self.zip:
                        return True
        else:
            return False
    
    def get_absolute_url(self):
        '''
        the URL referenced to display a user's information
        '''
        return "/students/%s" % self.id
    
    is_superuser = False
    is_staff = False
    
    objects = UserManager()
    
    def save(self):
        '''
        overriding the default save method from User
        '''
        password = ""
        r = re.compile('sha1\$.*')
        if not r.match(self.password):
            password = self.password
            self.set_password(self.password)
        User.save(self)
    
class StudentForm(ModelForm):
    '''
    defines a full-on student form object, with all User and Student model attributes
    '''    
    class Meta:
        model = Student

class StudentRegisterForm(ModelForm):
    '''
    an abbreviated form used for quick student registration
    '''
    class Meta:
        model = Student
        fields = ('username','first_name','last_name','email','password','favorite_subject','school')
    
class Teacher(User):
    '''
    The Teacher model represents all information tracked for a REGISTERED Teacher
    '''
    
    SALUTATION_CHOICES=(
                    ('Mr.','Mr.'),
                    ('Mrs.','Mrs.'),
                    ('Ms.','Ms.'),
                    ('Dr.','Dr.'),
                    )

    avatar = models.FileField(upload_to="avatars/teachers/", blank=True, help_text="Optional avatar you can upload")
    salutation = models.CharField(max_length=8, choices=SALUTATION_CHOICES, help_text="Your Preferred Title") 
    subjects_taught = models.ManyToManyField(Subject, help_text="Subject(s) Currently Taught by You")
    school = models.ForeignKey(School, help_text="The School You are Currently Attending")
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USPostalCodeField(blank=True, help_text="The State You Live In (Optional)")
    zip = models.CharField(max_length=10, blank=True, help_text="Your ZIP Code in XXXXX or XXXXX-XXXX Format (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    website = models.URLField(blank=True, help_text="Your Teacher Website (Optional)")
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")
    valid_email = models.BooleanField(default=True)

    is_superuser = False
    is_staff = False

    def is_teacher(self):
        """returns True because this is a Teacher object"""
        return True

    def has_valid_email(self):
        '''
        returns whether or not a teacher has a valid email address
        '''
        return self.valid_email

    def __unicode__(self):
        return "%s %s" % (str(self.salutation), self.last_name)
    
    def get_absolute_url(self):
        '''
        returns a relative URL for Teachers
        '''
        return "/teachers/%s" % self.id

    objects = UserManager()
    
    def save(self):
        '''
        overrides the default save function from User
        '''
        password = ""
        r = re.compile('sha1\$.*')
        if not r.match(self.password):
            password = self.password
            self.set_password(self.password)
        User.save(self)
    
class TeacherForm(ModelForm):
    '''
    represents a form that presents a full Teacher object.  Used for registration
    '''
    class Meta:
        model = Teacher

class Sponsor(User):
    '''
    The Sponsor model represents members of the community who can provide rewards for students and form relationships with teachers to provide incentives.
    '''

    avatar = models.FileField(upload_to="avatars/sponsors/", blank=True, help_text="Optional avatar you can upload", verbose_name="Company Logo")
    company_name= models.CharField(max_length=32, unique=True, help_text="Your Company Name")
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USPostalCodeField(blank=True, help_text="The State You Live In (Optional)")
    zip = models.CharField(max_length=10, blank=True, help_text="Your ZIP Code in XXXXX or XXXXX-XXXX Format (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    website = models.URLField(blank=True, help_text="Your Company Website (Optional)")
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")

    is_superuser = False
    is_staff = False

    def is_sponsor(self):
        """returns True because this is a Sponsor object"""
        return True

    def __unicode__(self):
        return self.company_name

    objects = UserManager()
    
    def save(self):
        '''
        Overrides the default save function from User
        '''
        password = ""
        r = re.compile('sha1\$.*')
        if not r.match(self.password):
            password = self.password
            self.set_password(self.password)
        User.save(self)

class SponsorForm(ModelForm):
    '''
    Provides a form for Sponsor Registration
    '''
    class Meta:
        model = Sponsor

class Mentor(User):
    '''
    The Mentor object in Goalfish represents outside professionals who can join to help mentor students in their goals and interests
    '''
    
    SALUTATION_CHOICES=(
                    ('Mr.','Mr.'),
                    ('Mrs.','Mrs.'),
                    ('Ms.','Ms.'),
                    ('Dr.','Dr.'),
                    )
    
    avatar = models.FileField(upload_to="avatars/mentors", blank=True, help_text="Optional avatar you can upload")
    alma_mater = models.ForeignKey(College, blank=True, help_text="College You Attend(ed) - Optional")
    professional_certifications = models.CharField(max_length=32, blank=True, help_text="Any Professional Certifications You Maintain")
    salutation = models.CharField(max_length=8, choices=SALUTATION_CHOICES, help_text="Your Desired Salutation") 
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USPostalCodeField(blank=True, help_text="The State You Live In (Optional)")
    zip = models.CharField(max_length=10, blank=True, help_text="Your ZIP Code in XXXXX or XXXXX-XXXX Format (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    website = models.URLField(blank=True, help_text="Your Website (Optional)")   
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")

    objects = UserManager()

    def is_mentor(self):
        """returns True because this is a Mentor object"""
        return True

    is_superuser = False
    is_staff = False
    
    def save(self):
        '''
        Overrides the defaul save function from User
        '''
        password = ""
        r = re.compile('sha1\$.*')
        if not r.match(self.password):
            password = self.password
            self.set_password(self.password)
        User.save(self)
        
class Mentorform(ModelForm):
    '''
    Provides a form for Mentor registration
    '''
    
    class Meta:
        model = Mentor
        
class Parent(User):
    '''
    Parents have a relatively limited role in Goalfish, essentially the ability to "morally compass" their children
    '''

    SALUTATION_CHOICES=(
                    ('Mr.','Mr.'),
                    ('Mrs.','Mrs.'),
                    ('Ms.','Ms.'),
                    ('Dr.','Dr.'),
                    )

    avatar = models.FileField(upload_to="avatars/parents", blank=True, help_text="Optional avatar you can upload")    
    salutation = models.CharField(max_length=8, choices=SALUTATION_CHOICES, help_text="Your Desired Salutation") 
    address1 = models.CharField(max_length=32, blank=True, help_text="Your Address (Optional)")
    address2 = models.CharField(max_length=32, blank=True, help_text="Your Address, Continued (Optional)")
    city = models.CharField(max_length=32, blank=True, help_text="The City You Live In (Optional)")
    state = USPostalCodeField(blank=True, help_text="The State You Live In (Optional)")
    zip = models.CharField(max_length=10, blank=True, help_text="Your ZIP Code in XXXXX or XXXXX-XXXX Format (Optional)")
    twitter = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Twitter Username (Optional)")
    facebook = models.CharField(max_length=64, blank=True, unique=True, help_text="Your Facebook Username (Optional)")
    sms = PhoneNumberField(blank=True, unique=True, help_text="Your SMS number to Receive Text Messages (Optional)")
    website = models.URLField(blank=True, help_text="Your Website (Optional)")    
    notes = models.TextField(blank=True, help_text="Optional Notes or a Description for Yourself")

    def is_parent(self):
        """returns True because this is a Parent object"""
        return True

    objects = UserManager()

    is_superuser = False
    is_staff = False
    
    def save(self):
        '''
        Overrides the default save function from User
        '''
        
        password = ""
        r = re.compile('sha1\$.*')
        if not r.match(self.password):
            password = self.password
            self.set_password(self.password)
        User.save(self)
    
class ParentForm(ModelForm):
    '''
    Provides a form for Parent Registration
    '''
    
    class Meta:
        model = Parent       
