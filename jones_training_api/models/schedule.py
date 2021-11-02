from django.contrib.auth.models import User
from django.db import models

class Schedule(models.Model):
    """Schedule Model
    Fields:
        user (ForeignKey): Id of the user who the schedule belongs to
        monday_tasks (CharField): The tasks assigned for monday
        tuesday_tasks (CharField): The tasks assigned for tuesday
        wednesday_tasks (CharField): The tasks assigned for wednesday
        thursday_tasks (CharField): The tasks assigned for thusday
        friday_tasks (CharField): The tasks assigned for friday
        saturday_tasks (CharField): The tasks assigned for saturday
        sunday_tasks (CharField): The tasks assigned for sunday
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monday_tasks = models.CharField(max_length=200)
    tuesday_tasks = models.CharField(max_length=200)
    wednesday_tasks = models.CharField(max_length=200)
    thursday_tasks = models.CharField(max_length=200)
    friday_tasks = models.CharField(max_length=200)
    saturday_tasks = models.CharField(max_length=200)
    sunday_tasks = models.CharField(max_length=200)