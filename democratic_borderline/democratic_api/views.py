from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from democratic_api.models import Person, BorderCrossing
from democratic_api.serializers import PersonBorderCrossingSerializer


class PersonBorderCrossing(viewsets.ViewSet):
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
        latest_person_crossed_border = latest_border_crossing.person

        serializer = PersonBorderCrossingSerializer(latest_person_crossed_border)
        return Response(serializer.data)
