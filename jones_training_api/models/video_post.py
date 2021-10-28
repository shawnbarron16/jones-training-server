from django.db import models

class video_post(models.Model):
    """Video Post Model
    Fields:
        title (CharField): The title of the video post
        description (CharField): The description fo the video post
        author (ForeignKey): The id of the user who posted the video
        is_premium (BooleanField): Determined if the post if for premium users only or not
        thumbnail (ImageField): The thumbnail used for the post
        video (FileField): The actual video for the post
    """

    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField
    thumbnail = models.ImageField(blank=True, null=True, upload_to="video_thumbnails")
    video = models.FileField(blank=True, null=True, upload_to="videos")

    def __str__(self):
        return self.title
