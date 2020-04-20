from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ExifTags

class Profile(models.Model):
    # CASCADE means that if the user is deleted from the db, delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default.jpg is the default image for any first-time registered user -> and send it to the directory called: profile_pics
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #Create a dunder str method so that when the image is printed out, it should be displayed accordingly the way it was programmed.
    def __str__(self):
        return f'{self.user.username} Profile'

    # This save method will run when the user updates the profile
    def save(self, *args, **kwargs):
        #Parent-class save method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)