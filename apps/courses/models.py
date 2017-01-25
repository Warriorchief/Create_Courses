from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length = 100)
    course_description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add = True)
    
