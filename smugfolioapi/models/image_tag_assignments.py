from django.db import models

class Image_Tag_Assignments(models.Model):
    
    image_tag_id = models.ForeignKey("Image_Tags", on_delete=models.CASCADE)
    image_id = models.ForeignKey("Images", on_delete=models.CASCADE)