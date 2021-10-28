from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import Field

class Friendship(models.Model):
    """Friendship Model
    Fields:

        user_id (Foreign Key): Id of the current user
        friend_id (Foreign Key): Id of the user the current user if friends with
        pending (Boolean): Determines if the friend request is pending or not
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pending = models.BooleanField(Field.default(True))