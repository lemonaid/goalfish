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
from Goalfish.academics.models import ScheduledClass

class RewardClass(models.Model):

    name = models.CharField(max_length=24, unique=True, help_text="Name for Reward Class")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class Reward(models.Model):

    name = models.CharField(max_length=24, unique=True, help_text="Reward Name")
    graphic = models.FileField(upload_to="/graphics/goals/", help_text="Graphic used to illustrate Reward")
    level = models.ForeignKey(RewardClass, help_text="Reward Level / Type")
    notes = models.TextField(blank=True, help_text="Optional Notes and Description")
    
    
    def __unicode__(self):
        return self.name
    
class AutomaticReward(models.Model):
    
    name = models.CharField(max_length=24, unique=True, help_text="Reward Name")
    graphic = models.FileField(upload_to="/graphics/goals/", help_text="Graphic used to illustrate Reward")
    condition = models.CharField(max_length=512, help_text="Condition(s) that activate this reward")
    notes = models.TextField(blank=True, help_text="Optional Notes and Description")   

    def __unicode__(self):
        return self.name

class StudentSMARTGoal(models.Model):
    
    GRADE_CHOICES=(
                   ('A','A'),
                   ('B','B'),
                   ('C','C'),
                   ('D','D'),
                   ('E','E'),
                   ('F','F'),
                   )

    name = models.CharField(max_length=64, help_text="A Name for Your Goal")
    goal_class = models.ForeignKey(ScheduledClass, help_text="Class this Goal Relates to")
    begin_grade = models.CharField(max_length=1, choices=GRADE_CHOICES, help_text="The Grade You are Starting With")
    ending_grade = models.CharField(max_length=1, choices=GRADE_CHOICES, help_text="The Grade You are Going to End With")
    begin_date = models.DateField(auto_now=False, help_text="When Your Goal Will Start")
    end_date = models.DateField(auto_now=False, help_text="When Your Goal Will Complete")
    reward = models.ForeignKey(Reward, help_text="What you will get for Your Reward")
    
#class TeacherAcademicGoal(models.Model):

#    name = models.CharField(max_length=64, help_text="Name for this Goal")
#    classroom = 
#    goal = 
#    reward = 