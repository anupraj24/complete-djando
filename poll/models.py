from typing import Text
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):

   text = models.TextField()
   author= models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
   pub_date = models.DateField(auto_now_add=True)
     

def __str__(self):
    return self.text

class Choice(models.Model):
    
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.TextField()
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voting_date = models.DateTimeField(auto_now_add=True)
    why = models.TextField(null=True, blank=True)
    


