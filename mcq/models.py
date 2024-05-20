from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    CHOICES = [(True,'Student'), (False,'Teacher')]
    user_type = models.BooleanField(default = False, choices = CHOICES)
    first_name = models.CharField(max_length = 30, blank = True, null = True)
    last_name = models.CharField(max_length = 30, blank = True, null = True)
    picture = models.ImageField(upload_to = 'images', blank = True, null = True)
    country = models.CharField(max_length = 20, blank = True, null = True)
    gender = models.CharField(max_length = 20, blank = True, null = True)
    phone = models.CharField(max_length = 20, blank = True, null = True)
    address = models.CharField(max_length = 100, blank = True, null = True)
    
    def __str__(self):
        return self.username
    
class Result(models.Model):
    StudentName = models.CharField(max_length = 100, blank = True, null = True)
    SubjectName = models.CharField(max_length = 100, blank = True, null = True)
    CntQuestion = models.IntegerField(blank = True, null = True)
    CntCorrectAns = models.IntegerField(blank = True, null = True)
    CntWrongAns = models.IntegerField(blank = True, null = True)
    SuccessRate = models.FloatField(blank = True, null = True)
    Grade = models.CharField(max_length = 10, blank = True, null = True)
    created_at = models.DateTimeField(blank = True, null = True)
    
    def __str__(self):
        return str(self.StudentName)
    

class AllQuestions(models.Model):
    question = models.CharField(max_length = 255)
    option_a = models.CharField(max_length = 255)
    option_b = models.CharField(max_length = 255)
    option_c = models.CharField(max_length = 255)
    option_d = models.CharField(max_length = 255)
    answer = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    
