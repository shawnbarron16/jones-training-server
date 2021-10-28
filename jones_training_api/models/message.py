from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import Field

class Message(models.Model):
    """Message Model
    Fields:
        sender_id (ForeignKey): Id of the user who sent the message
        recipient_id (ForeignKey): Id of the user who the message is being sent to
        read (BooleanField): Determines if the message has been read or not
        message (CharField): The actual contents of the message
    """

    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_id = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    message = models.CharField(max_length=5000)