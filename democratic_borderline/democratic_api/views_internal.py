from django.shortcuts import render
from rest_framework import viewsets

from democratic_api.models import BorderCrossing, ForbiddenStuff, Nationality, Person
from democratic_api.serializers import (
    BorderCrossingSerializer,
    ForbiddenStuffSerializer,
    NationalitySerializer,
    PersonSerializer,
)


class BorderCrossingViewSet(viewsets.ModelViewSet):
    queryset = BorderCrossing.objects.all()
    serializer_class = BorderCrossingSerializer


class ForbiddenStuffViewSet(viewsets.ModelViewSet):
    queryset = ForbiddenStuff.objects.all()
    serializer_class = ForbiddenStuffSerializer


class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
