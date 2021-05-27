from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        #generating random number from ascii
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        if Room.objects.filter(code = code).count() == 0:
            break
        #checking through the rooms to see if the code has been used

    return code


# Create your models here.

class Room(models.Model):
    #all of the below are components to skip 
    code = models.CharField(max_length =8, default ="", unique=True)
    host = models.CharField (max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null = False, default = False)
    #guest can pause , yes or no 
    votes_to_skip = models.IntegerField(null =False, default = 1)
    created_at = models.DateTimeField(auto_now_add=True) 
    #it will automatically add the date and time it was created at
    #put most of your logic on your models





