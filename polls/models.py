import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Question(models.Model):

    # Constante con las opciones para el campo category
    CATEGORY_CHOICES = [
        ('1', 'Category 1'),
        ('2', 'Category 2'),
        ('3', 'Category 3'),
        ('4', 'Category 4'),
        ('5', 'Category 5'),
    ]


    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # Campo de comentario opcional
    comment = models.TextField(blank=True, null=True)
    # Campo de categoría con opciones  
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=200, null=True, blank=True)  
    # Creacion de 2 campos que por defecto guarden la fecha y la hora de la creacion
    created_at = models.DateTimeField("date created", auto_now_add=True)
    update_date = models.DateTimeField("date updated", auto_now=True)
    pollster = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question_text
    
    # Constante para configurar los días considerados recientes
    RECENT_DAYS = 7 

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def save(self, *args, **kwargs):
        self.update_date = timezone.now()  
        super().save(*args, **kwargs)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # Creacion de 2 campos que por defecto guarden la fecha y la hora de la creacion
    created_at = models.DateTimeField("date created", auto_now_add=True)
    update_date = models.DateTimeField("date updated", auto_now=True)

    def __str__(self):
        return self.choice_text