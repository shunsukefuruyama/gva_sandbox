from django.db import models

class File(models.Model):
    name = models.CharField(max_length=10, default='default')
    file = models.FileField(upload_to='file/', blank=True, null=True)
