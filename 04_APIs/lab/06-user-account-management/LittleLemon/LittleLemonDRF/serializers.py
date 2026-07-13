from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    # Defaults to the authenticated user issuing the request, so clients
    # never have to (and can't) submit a user id themselves.
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Rating
        fields = ['user', 'menuitem_id', 'rating']

        validators = [
            # One rating per user per menu item; a second POST with the
            # same pair is rejected instead of creating a duplicate.
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields=['user', 'menuitem_id']
            )
        ]

        extra_kwargs = {
            'rating': {'min_value': 0, 'max_value': 5},
        }
