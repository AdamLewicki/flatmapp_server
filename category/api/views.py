import googlemaps
import sys

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from rest_framework import mixins
from rest_framework import generics


import os
import json
# Open settings file
settings_file = open("settings.json")
settings_data = json.load(settings_file)


class Category(APIView):

    def post(self, request):

        data = request.data

        gmaps = googlemaps.Client(key=settings_data.get("google_api_key"))

        try:
            if data.get('approximate') == True:
                places = gmaps.places(query=data.get("category"), 
                        location=(data.get("position_x"), data.get("position_y")), 
                        radius=data.get("range"), language="pl")
            else:
                places = gmaps.places_nearby(radius=data.get("range"), location=f"{data.get('position_x')}, {data.get('position_y')}", language="en", name=data.get("category"))
        except googlemaps.exceptions.ApiError:
            return Response({ data: "Category, range or position_x/position_y is missing"}, status=status.HTTP_400_BAD_REQUEST)

        places = places.get("results")

        output = dict()
        for index, place in enumerate(places):
            geometry = place.get("geometry")
            location = geometry.get("location")
            name = place.get("name")

            address = place.get("formatted_address")
            if address is None:
                address = place.get('vicinity')

            tmp = dict(addres=address, location=location, name=name)
            output[str(index)] = tmp


        data = {"data": output}
        return Response(data, status=status.HTTP_200_OK)