from django.db import models
from account.models import Account

# Create your models here.


class Action(models.Model):
    Action_Name = models.TextField()
    icon = models.TextField()
    action_position = models.IntegerField()
    action_detail = models.TextField()

    def __str__(self):
        return self.Action_Name
    
    class Meta:
        managed                 = True
        verbose_name            = 'Action'
        verbose_name_plural     = 'Actions'


class Pointer(models.Model):
    User_Name = models.ForeignKey(Account, on_delete=models.CASCADE)
    Action_Name = models.ManyToManyField(Action)

    queue = models.IntegerField()
    position_y = models.FloatField()
    position_x = models.FloatField()
    _range = models.FloatField()

    title = models.TextField()
    icon = models.TextField()
    description = models.TextField(blank=True)

    groupID = models.TextField(blank=True)


class Group(models.Model):
    User_Name = models.ForeignKey(Account, on_delete=models.CASCADE)

    groupID = models.TextField()
    _range = models.FloatField()
    name = models.TextField()
    Action_Name = models.ManyToManyField(Action)
