from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import Field

class Friendship(models.Model):
    """Friendship Model
    Fields:

        user (Foreign Key): Id of the current user
        friend (Foreign Key): Id of the user the current user if friends with
        pending (Boolean): Determines if the friend request is pending or not
    """
    user = models.ForeignKey(User, related_name='this_user', on_delete=models.CASCADE)
    added_friend = models.ForeignKey(User, related_name='added_friend', on_delete=models.CASCADE)
    pending = models.BooleanField(default=True)