from django.db import models
from rest_framework import serializers
from addressbook.constraints import ConstraintErrors
from authentication.models import User
from django_countries.data import COUNTRIES


def has_numbers(inputString):
    # TODO: need to add unit test on this
    return any(char.isdigit() for char in inputString)


def func(value):
    # TODO: need to add unit test on this
    if has_numbers(value):
        return value
    else:
        raise serializers.ValidationError(ConstraintErrors.NO_DIGITS_IN_POSTAL_CODE)


class Addressbook(models.Model):
    # TODO: country and city dropdown lists could be chained to depend on each other
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, default="")
    country = models.CharField(
        max_length=300, choices=sorted(COUNTRIES.items()), blank=True
    )
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50, validators=[func])

    # TODO: check this
    class Meta:
        unique_together = [
            "owner",
            "address_line_1",
            "address_line_2",
            "country",
            "city",
            "postcode",
        ]
