from django.db import models
class Images(models.Model):

    album_id = models.IntegerField(default=0)
    smug_user = models.ForeignKey("Smug_Users", on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(
        upload_to='smugimages', height_field=None,
        width_field=None, max_length=None, null=True
    )
    
    # @property
    # def imagecount(self):
    #     return self.__imagecount
    # @imagecount.setter
    # def imagecount(self, value):
    #     self.__imagecount = value
    
    # I believe that auto_now_add is the correct syntax. If I'm understanding this correctly, it only creates a timestamp when the object is first created.
    # https://www.geeksforgeeks.org/datetimefield-django-models/