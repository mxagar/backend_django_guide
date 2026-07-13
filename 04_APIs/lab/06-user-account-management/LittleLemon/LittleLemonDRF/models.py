from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    # CASCADE: deleting a user also deletes their ratings
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem_id = models.SmallIntegerField()
    rating = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{self.user} -> menuitem {self.menuitem_id}: {self.rating}"