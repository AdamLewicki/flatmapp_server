from django.contrib import admin

from .models import Marker, Action, Trigger, Tester
# Register your models here.


admin.site.register(Marker)
admin.site.register(Action)
admin.site.register(Trigger)

admin.site.register(Tester)