from rest_framework import serializers

from democratic_api.models import BorderCrossing, ForbiddenStuff, Nationality, Person


class BorderCrossingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorderCrossing
        fields = "__all__"


class ForbiddenStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForbiddenStuff
        fields = "__all__"


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
