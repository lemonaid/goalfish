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
from Goalfish.academics.models import Subject

class StudentSMARTGoal(models.Model):
    
    subject = models.ForeignKey(Subject, help_text="Subject this Goal Relates to")
    begin_grade = 
    ending_grade = 
    teacher = FK to teacher
    begin_date = auto_now
    end_date = 
    reward = FK to standard reward objects
    
class TeacherAcademicGoal(models.Model):

    classroom = FK to virtual classroom
    goal = 
    reward = 