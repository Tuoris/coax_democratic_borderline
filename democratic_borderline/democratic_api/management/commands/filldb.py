from django.core.management.base import BaseCommand, CommandError

from democratic_api.models import Nationality, BorderCrossing, ForbiddenStuff, Person


class Command(BaseCommand):
    help = "Fill database with mockup data"

    def handle(self, *args, **options):
        nationality_records = []
        for nationality in ("ukrainian", "british", "tai"):
            nationality_record = Nationality.objects.create(nationality=nationality)
            nationality_record.save()
            nationality_records.append(nationality_record)

        people = [
            {
                "first_name": "Kristofer",
                "last_name": "Robin",
                "date_of_birth": "1988-04-13",
                "living_address": "Ukraine, Lviv, Horbachevskogo, 21",
                "phone_number": "558033353535",
                "height": 1.72,
                "color_of_eyes": "blue",
                "married_to": None,
                "nationality": nationality_records[0],
            },
            {
                "first_name": "Maja",
                "last_name": "Rajesh",
                "date_of_birth": "1988-05-13",
                "living_address": "Ukraine, Lviv, Bandery, 111",
                "phone_number": "558033353534",
                "height": 1.80,
                "color_of_eyes": "red",
                "married_to": None,
                "nationality": nationality_records[1],
            },
        ]

        people_records = []
        for person in people:
            person_record = Person.objects.create(**person)
            person_record.save()
            people_records.append(person_record)

        borderline_crossings = [
            {"allowed": True, "person": people_records[0]},
            {"allowed": False, "person": people_records[1]},
        ]

        corssing_records = []
        for crossing in borderline_crossings:
            crossing_record = BorderCrossing.objects.create(**crossing)
            crossing_record.save()
            corssing_records.append(crossing_record)

        forbidden_stuff = [
            {
                "description": "Guns",
                "person": people_records[1],
                "border_crossing": corssing_records[1],
            },
            {
                "description": "Drugs",
                "person": people_records[1],
                "border_crossing": corssing_records[1],
            },
        ]

        for stuff in forbidden_stuff:
            stuff_record = ForbiddenStuff.objects.create(**stuff)
            stuff_record.save()

        self.stdout.write(self.style.SUCCESS("Successfully filled data "))
