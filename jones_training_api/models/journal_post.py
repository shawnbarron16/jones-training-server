from django.db import models

class Journal_Post(models.Model):
    """Journal Post Model
    Fields:
        title (CharField): The title of the post
        body (CharField): The actual content of the post
        author (ForeignKey): The id of the user who created the post
        thumbnail (ImageField) The image that gets associated with the post
    """

    title = models.CharField(max_length=300)
    body = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="journal_thumbnails")

    def __str__(self):
        return self.title