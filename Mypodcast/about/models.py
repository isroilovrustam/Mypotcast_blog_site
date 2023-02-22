from django.db import models

# Create your models here.


class About(models.Model):
    about_mypodcast = models.CharField(max_length=202)
    about_description = models.TextField()
    about_me_image = models.ImageField()
    about_me_description = models.TextField()

    def __str__(self):
        return self.about_mypodcast