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


class PersonBorderCrossingSerializer(serializers.ModelSerializer):
    class BorderCrossingSerializer(serializers.ModelSerializer):
        class Meta:
            model = BorderCrossing
            exclude = ["person"]

    class ForbiddenStuffSerializer(serializers.ModelSerializer):
        class Meta:
            model = ForbiddenStuff
            exclude = ["person", "border_crossing"]

    forbidden_stuff = ForbiddenStuffSerializer(many=True)
    border_crossing = BorderCrossingSerializer(many=True)

    class Meta:
        model = Person
        fields = "__all__"

    def create(self, validated_data):
        border_crossing_data = validated_data.pop("border_crossing", [None])[0]
        forbidden_stuff_data_list = validated_data.pop("forbidden_stuff")
        person_data = validated_data

        unique_field_set = (
            "first_name",
            "last_name",
            "date_of_birth",
            "living_address",
        )
        unique_person_query_params = {
            field: person_data[field] for field in unique_field_set
        }
        person = Person.objects.filter(**unique_person_query_params)

        if not person:
            person = Person.objects.create(**person_data)
        else:
            person = person.first()

        for key, value in person_data.items():
            setattr(person, key, value)
        person.save()

        if border_crossing_data:
            border_crossing = BorderCrossing.objects.create(
                person=person, **border_crossing_data
            )
        for forbidden_stuff_data in forbidden_stuff_data_list:
            ForbiddenStuff.objects.create(
                person=person, border_crossing=border_crossing, **forbidden_stuff_data
            )
        return person
