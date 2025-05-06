from django.db import models

class Image(models.Model):
    image_base64 = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.description