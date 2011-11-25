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

class RewardClass(models.Model):

    name = models.CharField(max_length=24, unique=True, help_text="Name for Reward Class")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class Reward(models.Model):

    name = models.CharField(max_length=24, unique=True, help_text="Reward Name")
    graphic = models.FileField(upload_to="graphics/goals/", help_text="Graphic used to illustrate Reward")
    level = models.ForeignKey(RewardClass, help_text="Reward Level / Type")
    notes = models.TextField(blank=True, help_text="Optional Notes and Description")
    
    
    def __unicode__(self):
        return self.name
