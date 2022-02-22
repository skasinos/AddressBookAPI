from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Addressbook
from addressbook.constraints import ConstraintErrors


class AddressbookSerializer(serializers.ModelSerializer):
    """
    It is assumed that a user can have an address record which is the same to another user, but that record is unique
    for each user.
    """

    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Addressbook
        fields = [
            "id",
            "url",
            "owner",
            "address_line_1",
            "address_line_2",
            "country",
            "city",
            "postcode",
        ]

        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                # TODO: a user is not currently allowed to add an address that exists in the system by another user
                fields=[
                    "owner",
                    "address_line_1",
                    "address_line_2",
                    "country",
                    "city",
                    "postcode",
                ],
                message=ConstraintErrors.DUPLICATED_USER_ADDRESS,
            )
        ]
