from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name=models.CharField(max_length=20)
    # image=models.FileField(upload_to="images")
    image=models.ImageField(upload_to="images")
	
