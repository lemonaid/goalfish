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
    """
    This provides a manageable list of Classes (Levels) to distinguish different groups of Reward objects
    """

    name = models.CharField(max_length=24, unique=True, help_text="Name for Reward Class")
    notes = models.TextField(blank=True, help_text="Optional Notes")
    
    def admin_notes(self):
        """A convention to allow HTML tags to show in the Django admin list display"""
        return self.notes
    
    admin_notes.allow_tags = True

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Goal Reward Level"
        verbose_name_plural = "Goal Reward Levels"

class Reward(models.Model):
    """
    This object provides a Reward object to relate to a goals.SMARTGoal or goals.TeacherAcademicGoal. This is typically a badge-type social reward that will show up on the child's homepage a la Foursquare et al
    """

    name = models.CharField(max_length=24, unique=True, help_text="Reward Name")
    graphic = models.ImageField(upload_to="graphics/goals/", help_text="Graphic used to illustrate Reward")
    level = models.ForeignKey(RewardClass, help_text="Reward Level / Type")
    notes = models.TextField(blank=True, help_text="Optional Notes and Description")
    
    def graphic_url(self):
        """Returns a link for the Django admin that links to the graphic URL for a given reward"""
        return "<a href='%s'>%s</a>" % (self.graphic.url, self.graphic.url)
    
    graphic_url.allow_tags = True
    
    def admin_notes(self):
        """A convention to allow HTML tags to show in the Django admin list display"""        
        return self.notes
    
    admin_notes.allow_tags = True        
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Goal Reward"
        verbose_name_plural = "Goal Rewards"