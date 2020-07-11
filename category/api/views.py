import googlemaps

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from rest_framework import mixins
from rest_framework import generics

class Category(APIView):

    def post(self, request):

        data = request.data


        gmaps = googlemaps.Client(key="")

        try:
            places = gmaps.places(query=data.get("category"), 
                    location=(data.get("position_x"), data.get("position_y")), 
                    radius=data.get("range"), language="pl")
        except googlemaps.exceptions.ApiError:
            return Response({ data: "Category, range or position_x/position_y is missing"}, status=status.HTTP_400_BAD_REQUEST)

        places = places.get("results")

        output = dict()
        for index, place in enumerate(places):
            geometry = place.get("geometry")
            location = geometry.get("location")
            radius = 176
            name = place.get("name")
            addres = place.get("formatted_address")

            tmp = dict(addres=addres, location=location, name=name, radius=radius)
            output[str(index)] = tmp


        data = {"data": output}
        return Response(data, status=status.HTTP_200_OK)