from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # CASCADE means that if the user is deleted from the db, delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default.jpg is the default image for any first-time registered user -> and send it to the directory called: profile_pics
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #Create a dunder str method so that when the image is printed out, it should be displayed accordingly the way it was programmed.
    def __str__(self):
        return f'{self.user.username} Profile'