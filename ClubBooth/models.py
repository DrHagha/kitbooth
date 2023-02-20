from django.db import models

# Create your models here.
class Booth(models.Model):
    booth_name = models.CharField(max_length=50, blank=True, default='')
    club_category = models.CharField(max_length=30, blank=True, default='무분류')
    club_picture = models.ImageField(default='/images/club_image/default_image.jpg')
    booth_location = models.CharField(max_length=5, blank=False, default='XX00')
    introduction = models.TextField()
    
    def __str__(self):
        return self.booth_name
    
