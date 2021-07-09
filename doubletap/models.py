from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

#user profile.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, default='0')
    profile_photo = CloudinaryField('image')
    bio = models.TextField()

    default=''
    #Profile methods
 
    def __str__(self):
        return self.user.user.name

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()  

# user post.
class Image(models.Model):
    image = CloudinaryField('images')
    image_name = models.CharField(max_length=30,blank=True)
    image_caption = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)
