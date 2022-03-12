from django.db import models
class Image_Tags(models.Model):
    
    image_tag_name = models.CharField(max_length=256)