from django.db import models
from smugfolioapi.models import image_tag_assignments, image_tags, Image_Tag_Assignments
class Images(models.Model):

    album_id = models.IntegerField(default=0)
    image_tags = models.ManyToManyField(image_tags.Image_Tags, through=Image_Tag_Assignments)
    smug_user = models.ForeignKey("Smug_Users", on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_name = models
    picture = models.ImageField(
        upload_to='smugimages', height_field=None,
        width_field=None, max_length=None, null=True
    )
    
    # picture key in the table is storing the file path, not the binary data, so I don't have worry about space constraints with the 100 character limit.
    
    # @property
    # def imagecount(self):
    #     return self.__imagecount
    # @imagecount.setter
    # def imagecount(self, value):
    #     self.__imagecount = value
    
    # I believe that auto_now_add is the correct syntax. If I'm understanding this correctly, it only creates a timestamp when the object is first created.
    # https://www.geeksforgeeks.org/datetimefield-django-models/