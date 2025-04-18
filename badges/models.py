from django.db import models

class Badge(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    earn_date = models.DateField()
    expiry_date = models.DateField()
    skills = models.JSONField()
    badge_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
