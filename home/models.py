from django.db import models
from django.utils.timezone import now

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images")
    description = models.TextField()
    url = models.URLField()
    date = models.DateTimeField(default=now)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['date']
