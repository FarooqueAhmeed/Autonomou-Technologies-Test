from django.db import models
from django.contrib.auth.models import User



class App(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=30)
        description = models.CharField(max_length=200)


        def __str__(self):
            return self.name


class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    app = models.ForeignKey(App, related_name='app', on_delete=models.DO_NOTHING, )

    Free = '$0'
    Standard = '$10'
    Pro = '$25'

    Plan_CHOICES = [
        (Free, '$0'),
        (Standard, '$10'),
        (Pro, '$25'),
    ]
    plan = models.CharField(
        max_length=5,
        choices=Plan_CHOICES,
        default=Free,
    )

    subscription = models.BooleanField(default=False)


    def __str__(self):
        return f' Plan - {self.plan} - To - {self.app} - Subscribed by -  {self.user}'