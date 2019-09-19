from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from democratic_api.models import Person, BorderCrossing
from democratic_api.serializers import PersonBorderCrossingSerializer


class PersonBorderCrossing(viewsets.ViewSet):
    """
    ## Create `BorderCrossing` for `Person` and update its info if changed

    ---

    ## Schema

    - `first_name` _string_ first name of a person

    - `last_name` _string_ last name of a person

    - `date_of_birth` _string_ date of birth of a person in ISO-8601 format (YYYY-MM-DD)

    - `living_address` _string_ adress of a person in arbitrary format

    - `phone_number` _integer_ phone number of a person, from 6 to 15 digits
    according to ITU-T E.164

    - `height` _float_ height of a person in meters

    - `color_of_eyes` _string_ color of a person eyes

    - `married_to` _string_, _nullable_ id of a person which are married to current
    person

    - `nationality` _integer_ id of a nationality of a person

    - `forbidden_stuff` _list_ list of forbidden stuff for a current border crossing,
    can be empty. Fields:
        - `description` _string_ description of forbidden stuff

    - `border_crossing` _list_ border crossing of a person. Can be empty, only
    first value is saved. Fields:
        - `date` _string_ **autogenerated** date and time of border crossing
        - `allowed` _boolean_ border crossing allowed/denied

    ---

    Example request:
        POST /api/person_border_crossing/
        Content-Type: application/json

        {
            "forbidden_stuff": [
                {"description": "Guns"},
                {"description": "Drugs"}
            ],
            "border_crossing": [
                {
                    "allowed": False
                }
            ],
            "first_name": "Kristofer",
            "last_name": "Robin",
            "date_of_birth": "1988-04-13",
            "living_address": "Ukraine, Lviv, Horbachevskogo, 21",
            "phone_number": "558033353535",
            "height": 1.72,
            "color_of_eyes": "blue",
            "married_to": null,
            "nationality": 2
        }

    This request will create new `Person` with attached new `BorderCrossing`
    for current date and time and with `ForbiddenStuff` if it's present.

    If `Person` already exist (has **same** `first_name`, `last_name`,
    `date_of_birth` and `living_address` fields) then request will attach new
    `BorderCrossing` for `Person` with current date and time and with
    `ForbiddenStuff`.
    """

    def list(self, request):
        queryset = Person.objects.all()
        serializer = PersonBorderCrossingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        person_border_crossing = get_object_or_404(queryset, pk=pk)
        serializer = PersonBorderCrossingSerializer(person_border_crossing)
        return Response(serializer.data)

    def create(self, request):
        serializer = PersonBorderCrossingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class LatestPersonCrossedBorder(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        latest_border_crossing = BorderCrossing.objects.all().order_by("-date").first()
        if latest_border_crossing:
            latest_person_crossed_border = latest_border_crossing.person
            serializer = PersonBorderCrossingSerializer(latest_person_crossed_border)
            return Response(serializer.data)
        return Response({})
