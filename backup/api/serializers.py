from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from backup.models import Action, Pointer, Group
from account.api.serializers import AccountSerializaer


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
        depth = 1


class PointerSerializer(WritableNestedModelSerializer):
    User_Name = AccountSerializaer(required=False, write_only=True)
    Action_Name = ActionSerializer(many=True)

    class Meta:
        model = Pointer
        depth = 1
        exclude = ("id",)


class GroupSerializer(WritableNestedModelSerializer):
    User_Name = AccountSerializaer(required=False, write_only=True)
    Action_Name = ActionSerializer(many=True)

    class Meta:
        model = Group
        depth = 1
        exclude = ("id",)
