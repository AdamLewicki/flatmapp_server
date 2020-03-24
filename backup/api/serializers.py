from rest_framework import serializers

from backup.models import Marker, Action, Trigger

class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = ['X_cord', 'Y_cord', 'Range', 'Info_title', 'Info_snipet']

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['Name',]

        