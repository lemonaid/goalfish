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
from Goalfish.academics.models import Grades
from Goalfish.rewards.models import Reward
from Goalfish.groups.models import Classes
from Goalfish.fishes.models import Student

class SMARTGoal(models.Model):
    #A SMART-process based Goal associated with a single Student.
    
    name = models.CharField(max_length=64, help_text="A Name for Your Goal")        
    student = models.ForeignKey(Student, related_name="student_goal")
    begin_grade = models.ForeignKey(Grades, related_name="begin_grade", help_text="The Grade You are Starting With")
    ending_grade = models.ForeignKey(Grades, related_name="ending_grade", help_text="The Grade You are Going to End With")
    begin_date = models.DateField(auto_now=False, help_text="When Your Goal Will Start")
    end_date = models.DateField(auto_now=False, help_text="When Your Goal Will Complete")
    reward = models.ForeignKey(Reward, help_text="A Reward for this Goal")
    active = models.BooleanField(default=True)
    complete = models.BooleanField()
    verified = models.BooleanField()
    
    def is_active(self):
        return self.active
    
    def is_complete(self):
        return self.complete
    
    def is_verified(self):
        return self.verified
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "SMART Goal"
        verbose_name_plural = "SMART Goals"
    
class TeacherAcademicGoal(models.Model):

    name = models.CharField(max_length=64, help_text="Name for this Goal")
    goal = models.TextField(help_text="A Brief Description of the Goal")
    reward = models.ForeignKey(Reward, help_text="A Reward for this Goal")
    associated_class = models.ForeignKey(Classes, help_text="Class This Goal is For")
    active = models.BooleanField(default=True)
    
    def is_active(self):
            return self.active
        
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Teacher Initiated Goal"
        verbose_name_plural = "Teacher Initiated Goals"
    
class AutoGoal(models.Model):
    
    name = models.CharField(max_length=24, unique=True, help_text="Reward Name")
    condition = models.CharField(max_length=512, help_text="Condition(s) that activate this reward")
    notes = models.TextField(blank=True, help_text="Optional Notes and Description") 
    recipients = models.ForeignKey(Student, help_text="Students Achieving This Goal")  
    reward = models.ForeignKey(Reward, help_text="A Reward for this Goal")
    active = models.BooleanField()
    
    def is_active(self):
        return self.active

    def activate(self):
        self.active = True
        self.save()

    def deactivate(self):
        self.active = False
        self.save()

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Automated Goal"
        verbose_name_plural = "Automated Goals"