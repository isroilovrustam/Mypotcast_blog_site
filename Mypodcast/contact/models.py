from django.db import models


# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=202)
    Email = models.EmailField()
    Subject = models.CharField(max_length=303)
    Message = models.TextField()

    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
