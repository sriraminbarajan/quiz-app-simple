import re
import json
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list
from django.conf import settings
from django.utils.translation import ugettext as _
from django.db.models.signals import pre_save, post_save
import io
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import models
from django.contrib import messages

# creating the model for category
class Catagory(models.Model):
    Quiz_category = models.CharField(max_length=50)

    def __str__(self):
        return self.Quiz_category
# creating the model for questions
class Questions(models.Model):
    
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    
    # used foreign key for referencing the category table 
    

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question




