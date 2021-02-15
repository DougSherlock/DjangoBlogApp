from django.db import models
from django.contrib.auth.models import User
from PIL import Image # import from the Pillow library

'''
Each model that is added must be registered by adding this line to the admin.py file for this app:
admin.site.register(Profile)
'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs): # overriding the default save function
        super().save(*args, **kwargs) # call the base class function

        # if the image is too large, make it smaller to save disk space
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



    