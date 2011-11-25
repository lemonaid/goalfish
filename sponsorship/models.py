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

class ItemType(models.Model):
    
    name = models.CharField(max_length=32, unique=True, help_text="Type of Item")
    notes = models.TextField(blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class SponsoredItem(models.Model):

    name = models.CharField(max_length=64, help_text="Name for this Sponsored Item")
    worth = models.IntegerField(max_length=4, help_text="Approximate Worth, in dollars")
    icon = models.FileField(upload_to="items/sponsored/", help_text="an icon to show on Goalfish for this item")
    start_date = models.DateField(auto_now=False, help_text="When the Item Becomes Valid")
    expire_date = models.DateField(auto_now=False, help_text="When the Item Becomes Invalid")
    mail_flag = models.BooleanField(help_text="If this item requires a mailing address")
    description = models.TextField(help_text="A description of the Item")
    
    def requires_mail(self):
        if self.mail_flag:
            return True    
    
    def __unicode__(self):
        return "%s-%s" % (str(self.sponsor), self.name)

