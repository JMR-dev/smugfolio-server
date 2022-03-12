from django.db import models
class Images(models.Model):

    file_name = models.CharField(max_length=1024)
    file_path = models.CharField(max_length=1024)
    album_id = models.IntegerField(default=0)
    smug_user_id = models.ForeignKey("Smug_Users", on_delete=models.CASCADE)
    upload_date = models.DateTimeField()