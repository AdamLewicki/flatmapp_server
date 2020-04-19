from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from rest_framework import mixins
from rest_framework import generics


from backup.models import Trigger
from backup.api.serializers import TriggerSerializer


class TriggerDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Trigger.objects.get(pk=pk)
        except Trigger.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trigger = self.get_object(pk)

        user = request.user
        if trigger.User_Id != user:
            return Response({'response':"You don't have permission to get that."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TriggerSerializer(trigger)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        trigger = self.get_object(pk)

        user = request.user
        if trigger.User_Id != user:
            return Response({'response':"You don't have permission to edit that."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TriggerSerializer(trigger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        trigger = self.get_object(pk)

        user = request.user
        if trigger.User_Id != user:
            return Response({'response':"You don't have permission to delete that."}, status=status.HTTP_403_FORBIDDEN)

        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TriggerList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        triggers = Trigger.objects.filter(User_Id=user)
        serializer = TriggerSerializer(triggers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        trigger = Trigger(User_Id=request.user)
        serializer = TriggerSerializer(trigger, data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)