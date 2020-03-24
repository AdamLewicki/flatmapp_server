from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from backup.models import Marker
from backup.api.serializers import MarkerSerializer


@api_view(['GET',])
def api_marker_detail_view(request, slug):
    try:
        marker = Marker.objects.get(pk=slug)
    except Marker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MarkerSerializer(marker)
        return Response(serializer.data)
    
@api_view(['POST',])
def api_marker_detail_post(request):
    if request.method == 'POST':
        serializer = MarkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_marker_detail_delete(request, slug):

    try:
        marker = Marker.objects.get(pk=slug)
    except Marker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = marker.delete()
        if operation:
            return Response(status=status.HTTP_200_OK)