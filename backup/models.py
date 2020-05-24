from django.db import models
from account.models import Account

# Create your models here.



class Marker(models.Model):
    X_cord                      = models.FloatField()
    Y_cord                      = models.FloatField()
    Range                       = models.FloatField()
    Info_title                  = models.CharField(max_length=64)
    Info_snipet                 = models.CharField(max_length=64)

    def __str__(self):
        return f"Marker {self.Info_title} at X: {self.X_cord} Y: {self.Y_cord} Descyption {self.Info_snipet[:25]}"

    class Meta:
        managed                 = True
        verbose_name            = 'Marker'
        verbose_name_plural     = 'Markers'

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

class Trigger(models.Model):
    User_Id                     = models.ForeignKey(Account, on_delete=models.CASCADE)
    Action_Id                   = models.ForeignKey(Action, on_delete=models.CASCADE)
    Marker_Id                   = models.ForeignKey(Marker, on_delete=models.CASCADE)


class Pointer(models.Model):
    User_Name = models.ForeignKey(Account, on_delete=models.CASCADE)
    Action_Name = models.ManyToManyField(Action)

    position_y = models.FloatField()
    position_x = models.FloatField()
    _range = models.FloatField()


    title = models.TextField()
    icon = models.TextField()
    description = models.TextField()

