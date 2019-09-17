from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class Nationality(models.Model):
    nationality = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.nationality)


class Person(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    married_to = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    living_address = models.CharField(max_length=256)
    phone_number = models.CharField(
        max_length=15, validators=[RegexValidator(r"^\d{6,15}$")]
    )
    height = models.FloatField(
        validators=[MinValueValidator(0.3), MaxValueValidator(3.0)]
    )
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)
    color_of_eyes = models.CharField(max_length=32)

    def __str__(self):
        return "{} {}, {}".format(self.first_name, self.last_name, self.date_of_birth)


class BorderCrossing(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    allowed = models.BooleanField()

    def __str__(self):
        return "{} {}, {}".format(
            self.person, self.date, "allowed" if self.allowed else "not allowed"
        )


class ForbiddenStuff(models.Model):
    description = models.CharField(max_length=256)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    border_crossing = models.ForeignKey(BorderCrossing, on_delete=models.CASCADE)

    def __str__(self):
        if self.description:
            return "{}".format(self.description[:32])
        return self.description
