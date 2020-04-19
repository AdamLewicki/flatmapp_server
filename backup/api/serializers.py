from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from backup.models import Marker, Action, Trigger, Tester
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

class TesterSerializer(WritableNestedModelSerializer):
    Action_Id = ActionSerializer()
    Marker_Id = MarkerSerializer()

    class Meta:
        model = Tester
        fields = "__all__"

class TriggerSerializer(WritableNestedModelSerializer):
    User_Id   = AccountSerializaer(required=False)
    Action_Id = ActionSerializer()
    Marker_Id = MarkerSerializer()

    class Meta:
        model = Tester
        fields = "__all__"
        depth = 2