from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from rest_framework import mixins
from rest_framework import generics

from backup.models import Pointer
from backup.api.serializers import PointerSerializer

from backup.models import Action


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
        for obj in request.data:
            pointer = Pointer(User_Name=request.user)
            serializer = PointerSerializer(pointer, data=obj)
            if serializer.is_valid():
                tmp = (serializer, pointer)
                to_save.append(tmp)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        self.delete(request)

        for tmp in to_save:
            tmp[0].save()

        data = {"Status" : ["OK"]}
        return Response(data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pointer = Pointer.objects.filter(User_Name=request.user)
        pointer.delete()
        
        data = {"Status" : ["OK"]}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
