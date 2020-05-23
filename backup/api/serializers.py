from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from backup.models import Marker, Action, Trigger, Pointer
from account.api.serializers import AccountSerializaer

class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = '__all__'
        depth = 1

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
        depth = 1

class TriggerSerializer(WritableNestedModelSerializer):
    User_Id   = AccountSerializaer(required=False)
    Action_Id = ActionSerializer()
    Marker_Id = MarkerSerializer()

    class Meta:
        model = Trigger
        fields = "__all__"
        depth = 2

class PointerSerializer(WritableNestedModelSerializer):
    User_Name = AccountSerializaer(required=False, write_only=True)
    Action_Name = ActionSerializer(many=True, read_only=True)

    class Meta:
        model = Pointer
        fields = "__all__"
        depth = 2