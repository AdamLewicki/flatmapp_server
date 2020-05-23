from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from rest_framework import mixins
from rest_framework import generics


from backup.models import Trigger
from backup.api.serializers import TriggerSerializer

from backup.models import Pointer
from backup.api.serializers import PointerSerializer

from backup.models import Action


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

        trigger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PointerList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        pointer = Pointer.objects.filter(User_Name=user)
        serializer = PointerSerializer(pointer, many=True)
        return Response(serializer.data)

    # method that saves multiple Pointers
    def post(self, request, format=None):

        to_save = list()
        # splits pointers data
        for obj in request.data:
            actions = obj.pop("Action_Name")
            actions = set(actions)
            pointer = Pointer(User_Name=request.user)
            serializer = PointerSerializer(pointer, data=obj)
            # check if Action exists in database, if not, stops saving
            for ack in actions:
                if not Action.objects.filter(Action_Name = ack):
                    data = {"Action_Name": [f"Action {ack} is not in the database"], "Status": ["ERROR"]}
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # checks if all serializers are valid, if not, stops saving
            if serializer.is_valid():
                tmp = (serializer, pointer, actions)
                to_save.append(tmp)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # we checked if serializers are valid and if actions exits in db, now we can save all pointers
            # also, to add Action_Name, a pointer must have pk, so we can add it only after saving    
        for tmp in to_save:
            tmp[0].save()
            tmp[1].Action_Name.set(tmp[2])

            data = {"Status" : ["OK"]}
            return Response(data, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        pointer = Pointer.objects.filter(User_Name=request.user)
        pointer.delete()
        
        data = {"Status" : ["OK"]}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
        