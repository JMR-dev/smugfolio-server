from django.db import models
class Images(models.Model):

    file_name = models.CharField(max_length=1024)
    file_path = models.CharField(max_length=1024)
    album_id = models.IntegerField(default=0)
    smug_user_id = models.ForeignKey("Smug_Users", on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    # I believe that auto_now_add is the correct syntax. If I'm understanding this correctly, it only creates a timestamp when the object is first created.
    # https://www.geeksforgeeks.org/datetimefield-django-models/