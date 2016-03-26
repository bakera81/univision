from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=255)
    datecreated=models.DateTimeField()    

    def __dir__(self):
        return [id, email, name, datecreated]

    def __unicode__(self):
        return self.email
