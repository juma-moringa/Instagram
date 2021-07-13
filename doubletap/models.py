from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

#user profile.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_photo = CloudinaryField('image')
    bio = models.TextField()

    default=''

    #Profile methods
 
    def __str__(self):
        return self.user.username
    
     #save method.
    def save_profile(self):
        self.user

     #search method.
    @classmethod
    def search_insta_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    @classmethod
    def update_profile(cls, id, profile_photo,bio):
        cls.objects.filter(id=id).update(profile_photo=profile_photo,bio=bio)
 
     #delete method.   
    def delete_profile(self):
        self.delete()  

# user post.
class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50,blank=True)
    image_caption = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)

     #Image methods
     #save the image method.
    def save_image(self):
        self.save()

    #delete the image method.
    def delete_image(self):
        self.delete()

   
    #update the image caption method.
    @classmethod
    def update_image_caption(cls, id, image_caption):
        cls.objects.filter(id=id).update(image_caption=image_caption)
 

    def __str__(self):
        return self.image_name


# user comments   pending//     
class Comment(models.Model):
    user= models.ForeignKey(Profile,on_delete=models.CASCADE)
    comment = models.TextField()
    post= models.ForeignKey(Image,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    
    #comments methods
    def save_comment(self):
        self.user

    def delete_comment(self):
        self.delete()

#follow 4 follow pending//
class Follow(models.Model):
    follower = models.ForeignKey(Profile,  related_name='following',on_delete=models.CASCADE)
    following = models.ForeignKey(Profile,related_name='followers',on_delete=models.CASCADE)
