import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    choices_status = (('1', 'Ativo'),
                      ('0', 'Inativo'))
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    status = models.CharField(max_length=1, choices=choices_status, default='1')
    sequence = models.IntegerField(default=0)
    @admin.display(
            boolean=True,
            ordering='pub_date',
            description='Published recently?',
        )
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text